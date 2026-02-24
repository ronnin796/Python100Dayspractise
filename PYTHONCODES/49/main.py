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


def summary(
    booking_count=0, booked_waitlisted=0, waitlists_joined=0, total_classes=0, date=""
):
    print(
        f"""--- BOOKING SUMMARY ---
Classes booked: {booking_count}
Waitlists joined: {waitlists_joined}
Already booked/waitlisted: {booked_waitlisted}
Total {date} classes processed: {total_classes}
"""
    )


def book_tuesday():
    booking_count = 0
    booked_waitlisted = 0
    waitlists_joined = 0

    try:
        tuesday_section = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//h2[contains(text(),'Tue')]/parent::div")
            )
        )
        date = tuesday_section.find_element(
            By.XPATH, ".//h2[contains(@class,'Schedule_dayTitle')]"
        )

        buttons = tuesday_section.find_elements(
            By.XPATH,
            ".//button[contains(@class,'ClassCard_bookButton')]",
        )
        count = 0

        if not buttons:
            print("No Tuesday classes found.")
            return

        for button in buttons:
            try:
                driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center'});", button
                )
                class_names = tuesday_section.find_elements(
                    By.XPATH,
                    ".//h3[contains(@id,'class-name')]",
                )

                text = button.text.strip()

                if "Booked" in text:
                    print(f"Already Booked {class_names[count].text} at {date.text}")
                    booked_waitlisted += 1
                    continue

                elif "Join Waitlist" in text:
                    wait.until(EC.element_to_be_clickable(button))
                    button.click()
                    print("Joined waitlist.")
                    waitlists_joined += 1
                    wait.until(
                        lambda d: "Waitlisted" in button.text or "Leave" in button.text
                    )
                    return

                elif "Book Class" in text:
                    wait.until(EC.element_to_be_clickable(button))
                    button.click()
                    print("Booked class.")
                    booking_count += 1

                    wait.until(lambda d: "Booked" in button.text)
                    return
                elif "Waitlisted" in text:
                    print("Waitlisted")
                    booked_waitlisted += 1
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
            count += 1

    except TimeoutException:
        print("Tuesday section not found.")
    finally:
        summary(
            booked_waitlisted,
            waitlists_joined,
            total_classes=len(buttons),
            date=date.text,
        )


book_tuesday()
