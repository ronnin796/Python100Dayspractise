from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

options = Options()
# options.add_argument("--headless=new")
options.binary_location = "/usr/bin/brave-browser"

driver = webdriver.Chrome(options=options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

# Use find_element (not find_elements)
first_name = driver.find_element(By.NAME, "fName")
last_name = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")

# Correct method name: send_keys
first_name.send_keys("Nischal")
last_name.send_keys("Chaudhary")
email.send_keys("nischal@example.com")

# Submit form
email.send_keys(Keys.ENTER)

driver.quit()
