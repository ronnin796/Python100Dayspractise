from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    NoSuchElementException,
)
import time

EMAIL = BLA_BLA_BLA
PASSWORD = BLA_BLA_BLA


# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

# Move the Webdriver Chrome on second monitor
driver.set_window_position(-1000, 0)

# Maximize the window and proceed to Tinder
driver.maximize_window()
driver.get("https://www.tinder.com/")

# Log in button
time.sleep(1)
login_button = driver.find_element(By.LINK_TEXT, value="Log in")
login_button.click()

# Select Log in with Facebook
time.sleep(1)
login_with_facebook = driver.find_element(
    By.CSS_SELECTOR, value="button[aria-label='Log in with Facebook']"
)
login_with_facebook.click()

# Switch to Facebook window
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

# Sign in to Facebook
email_input = driver.find_element(By.ID, value="email")
email_input.send_keys(EMAIL)

password_input = driver.find_element(By.ID, value="pass")
password_input.send_keys(PASSWORD)
password_input.send_keys(Keys.ENTER)

# Switch back to Tinder window
driver.switch_to.window(base_window)
print(driver.title)

# Tinder Setup - sleeping for 8 seconds to load everything
time.sleep(8)
allow_location_button = driver.find_element(
    By.CSS_SELECTOR, value="button[aria-label='Allow']"
)
allow_location_button.click()

time.sleep(2)
miss_out_button = driver.find_element(
    By.CSS_SELECTOR, value="button[aria-label='I’ll miss out']"
)
miss_out_button.click()

time.sleep(2)
decline_cookies = driver.find_element(
    By.XPATH,
    value="//*[@id='t2067052097']/div/div[2]/div/div/div[1]/div[2]/button/div[2]/div[2]/div",
)
decline_cookies.click()

# Tinder free tier only allows 100 "Likes" per day.
for n in range(100):

    # Add a 2-second delay between likes.
    time.sleep(2)

    try:
        print("Clicking the Like button...")
        heart_icon = driver.find_element(
            By.XPATH,
            value="//*[@id='t2067052097']/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div/div[4]/button",
        )
        heart_icon.click()

    # For "It's a match" pop-up!
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, value=".itsAMatch a")
            match_popup.click()
        # For "Tinder Gold" pop-up
        except NoSuchElementException:
            close_tinder_gold = driver.find_element(
                By.XPATH, value="//*[@id='t338671021']/div/div[2]/div[2]/button"
            )
            close_tinder_gold.click()

    # If the Like button changes XPath after the first Like
    except NoSuchElementException:
        try:
            heart_icon = driver.find_element(
                By.XPATH,
                value="//*[@id='t2067052097']/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button",
            )
            heart_icon.click()
        # For "Add Tinder to your Home Screen" pop-up
        except ElementClickInterceptedException:
            not_interested_button = driver.find_element(
                By.XPATH,
                value="//*[@id='t338671021']/div/div/div[2]/button[2]/div[2]/div[2]/div",
            )
            not_interested_button.click()

driver.quit()
