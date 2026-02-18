from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless=new")

options.binary_location = "/usr/bin/brave-browser"

driver = webdriver.Chrome(options=options)
driver.get("https://www.python.org/")

dates = driver.find_elements(
    By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[2]/time/span'
)

event_date = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget  li a")

event_list = {
    i: {"date": event_date[i].text, "event_name": event_names[i].text}
    for i in range(len(event_date) - 1)
}
print(event_list)
# for date in event_date:
#     print(date.text)
# for names in event_names:
#     print(names.text)

# print(dates)
