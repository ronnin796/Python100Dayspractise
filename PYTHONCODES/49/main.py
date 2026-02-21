from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException

ACCOUNT_EMAIL = "noctis@gmail.com"
ACCOUNT_PASSWORD = "nocits1234"

options = Options()
options.add_experimental_option("detach", True)
options.binary_location = "/usr/bin/brave-browser"
options.add_argument(
    "--user-data-dir=/home/ronninx/.config/BraveSoftware/Brave-Browser"
)
options.add_argument("--profile-directory=Profile 1")

driver = webdriver.Chrome(options=options)
driver.get("https://appbrewery.github.io/gym/")

wait = WebDriverWait(driver, 10)

# Click login button first (if needed)
login_button = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
login_button.click()

# Wait for form fields
email_field = wait.until(EC.presence_of_element_located((By.ID, "email-input")))
password_field = wait.until(EC.presence_of_element_located((By.ID, "password-input")))
submit_button = wait.until(EC.element_to_be_clickable((By.ID, "submit-button")))

# Login
email_field.send_keys(ACCOUNT_EMAIL)
password_field.send_keys(ACCOUNT_PASSWORD)
submit_button.click()


# Book tuesday classes
def book_tuesday():
    # Wait for at least one Tuesday available button
    wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//h2[contains(@id,'day-title-tue')]/following-sibling::div//button[contains(@class,'ClassCard_available__')]",
            )
        )
    )

    book_buttons = driver.find_elements(
        By.XPATH,
        "//h2[contains(@id,'day-title-tue')]/following-sibling::div//button[contains(@class,'ClassCard_available__')]",
    )

    for button in book_buttons:
        try:
            driver.execute_script("arguments[0].scrollIntoView(true);", button)
            wait.until(EC.element_to_be_clickable(button))
            button.click()
        except ElementClickInterceptedException:
            driver.execute_script("arguments[0].click();", button)


book_tuesday()
