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


from selenium.common.exceptions import (
    ElementClickInterceptedException,
    StaleElementReferenceException,
    TimeoutException,
)


def book_tuesday():
    # Target ONLY buttons that don't say "Booked" yet
    tuesday_buttons_xpath = (
        "//h2[contains(text(),'Tuesday')]"
        "/following-sibling::div"
        "//button[contains(@class,'ClassCard_available__') and not(contains(., 'Booked'))]"
    )

    while True:
        try:
            # Re-fetch elements every time the loop restarts to avoid staleness
            wait.until(
                EC.presence_of_element_located((By.XPATH, tuesday_buttons_xpath))
            )
            buttons = driver.find_elements(By.XPATH, tuesday_buttons_xpath)

            if not buttons:
                print("No more available Tuesday classes.")
                break

            # Click only the FIRST available button found
            button = buttons[0]

            driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});", button
            )

            try:
                # Attempt a clean click
                wait.until(EC.element_to_be_clickable(button))
                button.click()
            except (ElementClickInterceptedException, StaleElementReferenceException):
                # Fallback to JS click if something is overlapping
                driver.execute_script("arguments[0].click();", button)

            print("Booked a class. Refreshing list...")

            # CRITICAL: Wait for the DOM to update or for the button to change state
            # This prevents the loop from grabbing the same button again
            wait.until(EC.staleness_of(button))

        except TimeoutException:
            print("Finished booking or timed out.")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break


book_tuesday()
