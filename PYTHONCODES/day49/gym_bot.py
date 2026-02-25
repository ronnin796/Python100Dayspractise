from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    StaleElementReferenceException,
    TimeoutException,
)

ACCOUNT_EMAIL = "noctis@gmail.com"
ACCOUNT_PASSWORD = "nocits1234"

# ------------------ BROWSER SETUP ------------------

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

# ------------------ LOGIN ------------------


def login(driver, wait, email, password):
    login_button = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
    login_button.click()

    email_field = wait.until(EC.presence_of_element_located((By.ID, "email-input")))
    password_field = wait.until(
        EC.presence_of_element_located((By.ID, "password-input"))
    )
    submit_button = wait.until(EC.element_to_be_clickable((By.ID, "submit-button")))

    email_field.send_keys(email)
    password_field.send_keys(password)
    submit_button.click()


login(driver, wait, ACCOUNT_EMAIL, ACCOUNT_PASSWORD)
# ------------------ SUMMARY FUNCTION ------------------
total_bookings = 0


def summary(
    booking_count=0, booked_waitlisted=0, waitlists_joined=0, total_classes=0, date=""
):
    print(
        f"""
--- BOOKING SUMMARY ---
Date: {date}
Classes booked: {booking_count}
Waitlists joined: {waitlists_joined}
Already booked/waitlisted: {booked_waitlisted}
Total classes processed: {total_classes}
"""
    )


def verify_bookings(expected_bookings, total_bookings):
    if expected_bookings == total_bookings:
        print(f"Bookings verified")


# ------------------ BOOK DAY FUNCTION ------------------


def book_day(day: str):
    global total_bookings
    booking_count = 0
    booked_waitlisted = 0
    waitlists_joined = 0
    buttons = []
    date_text = day

    try:
        day_section = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, f"//h2[contains(text(),'{day}')]/parent::div")
            )
        )

        date_element = day_section.find_element(
            By.XPATH, ".//h2[contains(@class,'Schedule_dayTitle')]"
        )
        date_text = date_element.text

        buttons = day_section.find_elements(
            By.XPATH,
            ".//button[contains(@class,'ClassCard_bookButton')]",
        )

        class_names = day_section.find_elements(
            By.XPATH,
            ".//h3[contains(@id,'class-name')]",
        )

        if not buttons:
            print(f"No {day} classes found.")
            return

        for index, button in enumerate(buttons):

            try:
                driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center'});", button
                )

                text = button.text.strip()
                class_name = (
                    class_names[index].text
                    if index < len(class_names)
                    else "Unknown Class"
                )

                if "Booked" in text:
                    print(f"Already Booked: {class_name} at {date_text}")
                    booked_waitlisted += 1
                    total_bookings += 1

                elif "Join Waitlist" in text:
                    wait.until(EC.element_to_be_clickable(button))
                    button.click()
                    print(f"Joined waitlist: {class_name}")
                    waitlists_joined += 1
                    wait.until(lambda d: "Waitlisted" in button.text)

                elif "Book Class" in text:
                    wait.until(EC.element_to_be_clickable(button))
                    button.click()
                    print(f"Booked class: {class_name} at {date_text}")
                    booking_count += 1
                    total_bookings += 1
                    wait.until(lambda d: "Booked" in button.text)

                elif "Waitlisted" in text:
                    print(f"Already waitlisted: {class_name}")
                    booked_waitlisted += 1

                else:
                    print(f"Unknown button state: {text}")

            except ElementClickInterceptedException:
                driver.execute_script("arguments[0].click();", button)
                print("Clicked using JS fallback.")

            except StaleElementReferenceException:
                print("Element went stale, continuing...")
                continue

    except TimeoutException:
        print(f"{day} section not found.")

    finally:
        summary(
            booking_count=booking_count,
            booked_waitlisted=booked_waitlisted,
            waitlists_joined=waitlists_joined,
            total_classes=len(buttons),
            date=date_text,
        )
