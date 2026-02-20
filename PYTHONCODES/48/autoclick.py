from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

options = Options()
# options.add_argument("--headless=new")
options.binary_location = "/usr/bin/brave-browser"

driver = webdriver.Chrome(options=options)

driver.get("https://ozh.github.io/cookieclicker/")
wait = WebDriverWait(driver, 10)
lang_button = wait.until(EC.element_to_be_clickable((By.ID, "langSelect-EN")))
lang_button.click()
cookie_counter = driver.find_element(By.ID, "cookies")
# Use find_element (not find_elements)
cookie = wait.until(EC.element_to_be_clickable((By.ID, "bigCookie")))


def get_cookie_count():
    text = cookie_counter.text
    number = text.split(" ")[0]
    number = number.replace(",", "")
    return int(number)


def buy_upgrades():
    upgrades = driver.find_elements(By.CSS_SELECTOR, ".product.unlocked.enabled")
    if upgrades:
        upgrades[-1].click()


start_time = time.time()
timeout = start_time + 60 * 20

while time.time() < timeout:
    cookie.click()
    if time.time() - start_time >= 5:
        print("5 seconds have passed")
        start_time = time.time()
        buy_upgrades()

driver.quit()
