from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    StaleElementReferenceException,
    TimeoutException,
)

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


def book_tuesday():
    try:
        tuesday_section = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//h2[contains(text(),'Tue')]/parent::div")
            )
        )

        buttons = tuesday_section.find_elements(
            By.XPATH,
            ".//button[contains(@class,'ClassCard_bookButton')]",
        )

        if not buttons:
            print("No Tuesday classes found.")
            return

        for button in buttons:
            try:
                driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center'});", button
                )

                text = button.text.strip()

                if "Booked" in text:
                    print("Already booked.")
                    continue

                elif "Join Waitlist" in text:
                    wait.until(EC.element_to_be_clickable(button))
                    button.click()
                    print("Joined waitlist.")

                    wait.until(
                        lambda d: "Waitlisted" in button.text or "Leave" in button.text
                    )
                    return

                elif "Book Class" in text:
                    wait.until(EC.element_to_be_clickable(button))
                    button.click()
                    print("Booked class.")

                    wait.until(lambda d: "Booked" in button.text)
                    return
                elif "Waitlisted" in text:
                    print("Waitlisted")
                    continue

                else:
                    print(f"Unknown button state: {text}")

            except ElementClickInterceptedException:
                driver.execute_script("arguments[0].click();", button)
                print("Clicked using JS.")
                return

            except StaleElementReferenceException:
                print("Element went stale, retrying...")
                return book_tuesday()

        print("No actionable Tuesday classes found.")

    except TimeoutException:
        print("Tuesday section not found.")


book_tuesday()
