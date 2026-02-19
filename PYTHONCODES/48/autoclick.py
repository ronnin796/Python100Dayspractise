from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

options = Options()
# options.add_argument("--headless=new")
options.binary_location = "/usr/bin/brave-browser"

driver = webdriver.Chrome(options=options)

driver.get("https://ozh.github.io/cookieclicker/")
wait = WebDriverWait(driver, 10)
lang_button = wait.until(EC.element_to_be_clickable((By.ID, "langSelect-EN")))
lang_button.click()

# Use find_element (not find_elements)
cookie = wait.until(EC.element_to_be_clickable((By.ID, "bigCookie")))
while True:
    cookie.click()

# Correct method name: send_keys
cookie.send_keys(Keys.ENTER)

# Submit form


driver.quit()
