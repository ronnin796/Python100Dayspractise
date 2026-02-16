from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless=new")
# Tell Selenium to use Brave instead of Chrome
options.binary_location = "/usr/bin/brave-browser"

driver = webdriver.Chrome(options=options)
driver.get("https://www.billboard.com/charts/hot-100/")

songs = driver.find_elements(By.CSS_SELECTOR, "h3#title-of-a-story")

for song in songs:
    print(song.text.strip())


driver.quit()
