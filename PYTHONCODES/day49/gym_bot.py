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


class GymBot:
    def __init__(self, email, password):
        self.email = email
        self.password = password

        # Separate tracking variables
        self.total_confirmed = 0
        self.total_waitlisted = 0

        self.driver = self._setup_driver()
        self.wait = WebDriverWait(self.driver, 10)

    # ------------------ DRIVER SETUP ------------------

    def _setup_driver(self):
        options = Options()
        options.add_experimental_option("detach", True)
        options.binary_location = "/usr/bin/brave-browser"
        options.add_argument(
            "--user-data-dir=/home/ronninx/.config/BraveSoftware/Brave-Browser"
        )
        options.add_argument("--profile-directory=Profile 1")

        driver = webdriver.Chrome(options=options)
        driver.get("https://appbrewery.github.io/gym/")
        return driver

    # ------------------ LOGIN ------------------

    def login(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, "login-button"))).click()

        self.wait.until(
            EC.presence_of_element_located((By.ID, "email-input"))
        ).send_keys(self.email)

        self.wait.until(
            EC.presence_of_element_located((By.ID, "password-input"))
        ).send_keys(self.password)

        self.wait.until(EC.element_to_be_clickable((By.ID, "submit-button"))).click()

    # ------------------ SUMMARY ------------------

    def summary(
        self, booking_count, booked_waitlisted, waitlists_joined, total_classes, date
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

    # ------------------ BOOK DAY ------------------

    def book_day(self, day: str):
        booking_count = 0
        booked_waitlisted = 0
        waitlists_joined = 0
        buttons = []
        date_text = day

        try:
            day_section = self.wait.until(
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
                    self.driver.execute_script(
                        "arguments[0].scrollIntoView({block:'center'});",
                        button,
                    )

                    text = button.text.strip()
                    class_name = (
                        class_names[index].text
                        if index < len(class_names)
                        else "Unknown Class"
                    )

                    # Already confirmed
                    if "Booked" in text:
                        print(f"Already Booked: {class_name} at {date_text}")
                        booked_waitlisted += 1
                        self.total_confirmed += 1

                    # Join waitlist
                    elif "Join Waitlist" in text:
                        self.wait.until(EC.element_to_be_clickable(button))
                        button.click()
                        print(f"Joined waitlist: {class_name}")
                        waitlists_joined += 1
                        self.total_waitlisted += 1
                        self.wait.until(lambda d: "Waitlisted" in button.text)

                    # Book class
                    elif "Book Class" in text:
                        self.wait.until(EC.element_to_be_clickable(button))
                        button.click()
                        print(f"Booked class: {class_name} at {date_text}")
                        booking_count += 1
                        self.total_confirmed += 1
                        self.wait.until(lambda d: "Booked" in button.text)

                    # Already waitlisted
                    elif "Waitlisted" in text:
                        print(f"Already waitlisted: {class_name}")
                        booked_waitlisted += 1
                        self.total_waitlisted += 1

                    else:
                        print(f"Unknown button state: {text}")

                except ElementClickInterceptedException:
                    self.driver.execute_script("arguments[0].click();", button)
                    print("Clicked using JS fallback.")

                except StaleElementReferenceException:
                    print("Element went stale, continuing...")
                    continue

        except TimeoutException:
            print(f"{day} section not found.")

        finally:
            self.summary(
                booking_count,
                booked_waitlisted,
                waitlists_joined,
                len(buttons),
                date_text,
            )

    # ------------------ VERIFY BOOKINGS ------------------

    def verify_bookings(self):
        # Navigate to My Bookings
        self.wait.until(EC.element_to_be_clickable((By.ID, "my-bookings-link"))).click()

        # ---------- CONFIRMED BOOKINGS ----------
        confirmed_section = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//h2[contains(text(),'Confirmed Bookings')]/parent::div")
            )
        )

        confirmed_cards = confirmed_section.find_elements(
            By.XPATH, ".//*[contains(@id,'booking-card')]"
        )

        confirmed_count = len(confirmed_cards)

        # ---------- WAITLIST BOOKINGS ----------
        waitlist_section = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//h2[@id='waitlist-title']/parent::div")
            )
        )

        waitlist_cards = waitlist_section.find_elements(
            By.XPATH, ".//*[contains(@id,'waitlist-card')]"
        )

        waitlist_count = len(waitlist_cards)

        # ---------- RESULTS ----------
        print("\n--- VERIFICATION RESULTS ---")
        print(f"Expected Confirmed: {self.total_confirmed}")
        print(f"Actual Confirmed:   {confirmed_count}")
        print(f"Expected Waitlist:  {self.total_waitlisted}")
        print(f"Actual Waitlist:    {waitlist_count}")

        if (
            confirmed_count == self.total_confirmed
            and waitlist_count == self.total_waitlisted
        ):
            print("All bookings verified successfully ✅")
        else:
            print("Booking mismatch detected ❌")

    # ------------------ CLOSE ------------------

    def close(self):
        self.driver.quit()


# ------------------ RUN SCRIPT ------------------

if __name__ == "__main__":
    bot = GymBot("noctis@gmail.com", "nocits1234")

    bot.login()

    bot.book_day("Tue")
    bot.book_day("Thu")

    bot.verify_bookings()

    # Optional: bot.close()
