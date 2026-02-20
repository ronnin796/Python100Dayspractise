import os
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

driver.get("https://appbrewery.github.io/gym/")
wait = WebDriverWait(driver, 10)
driver.quit()
