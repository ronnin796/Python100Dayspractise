from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
import time
from decouple import config
import re

RENTAL_LINK = "https://appbrewery.github.io/Zillow-Clone/"
SHEET_LINK = config("SHEET_URL")


class rentalListing:
    def __init__(self, rentlink=RENTAL_LINK, SHEET_LINK=SHEET_LINK):
        self.rentlink = rentlink
        self.driver = self._setup_driver()
        self.wait = WebDriverWait(self.driver, 10)
        self.address_list = []
        self.rent_prices = []
        self.links = []

    def _setup_driver(self):
        options = Options()
        options.add_experimental_option("detach", True)
        options.binary_location = "/usr/bin/brave-browser"
        options.add_argument(
            "--user-data-dir=/home/ronninx/.config/BraveSoftware/Brave-Browser"
        )
        options.add_argument("--profile-directory=Profile 1")

        return webdriver.Chrome(options=options)

    def get_rentdata(self):
        self.driver.get(self.rentlink)

        self.wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "ul[class*='photo-cards']")
            )
        )

        items = self.driver.find_elements(
            By.CSS_SELECTOR, "ul[class*='photo-cards'] > li"
        )

        for item in items:
            try:

                price_element = item.find_element(
                    By.CSS_SELECTOR, "[data-test='property-card-price']"
                )
                raw_price = price_element.text

                price_number = re.search(r"\d[\d,]*", raw_price)
                if price_number:
                    cleaned_price = price_number.group().replace(",", "")
                else:
                    cleaned_price = None

                address = item.find_element(
                    By.CSS_SELECTOR, "[data-test='property-card-addr']"
                ).text

                link = item.find_element(
                    By.CSS_SELECTOR, "[data-test='property-card-link']"
                ).get_attribute("href")

                print("Price:", cleaned_price)
                print("Address:", address)
                print("Link:", link)
                print("-" * 50)

            except Exception:
                continue

    def close(self):
        self.driver.quit()


if __name__ == "__main__":
    bot = rentalListing()
    bot.get_rentdata()
    bot.close()
