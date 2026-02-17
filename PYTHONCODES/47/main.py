from email import message
from bs4 import BeautifulSoup
import requests
from sendmail import send_mail

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
}
amazon_url = (
    "https://www.amazon.com/Lenovo-Legion-Gaming-GeForce-Windows/dp/B0FL4HLJ56/"
)


class Amazon_price:
    def __init__(self, headers=headers, url=amazon_url) -> None:
        self.url = url
        self.headers = headers

    def scrape_site(self) -> [any]:
        return requests.get(url=self.url, headers=self.headers)

    def get_title(self):
        response = requests.get(url=self.url, headers=self.headers)
        soup = self.soupify(response)
        return soup.find("span", id="productTitle").get_text(strip=True)

    def fetch_price(
        self, tag: str = "span", class_: str = "a-price-whole", *args: str
    ) -> str:
        response = self.scrape_site()
        soup = self.soupify(response)
        price_tag = soup.find(tag, class_=class_)
        if price_tag:
            return price_tag.get_text()
        else:
            print("Price not found. Amazon may be blocking requests.")

    def soupify(self, response, parser="html.parser") -> any:
        return BeautifulSoup(response.content, parser)


amz = Amazon_price()
price_str = amz.fetch_price()  # e.g., "1,299.50"
price_float = float(price_str.replace(",", ""))
acceptable_price = 2500
title = amz.get_title()

if price_float <= acceptable_price:
    message = (
        f"the price of {title} has been dropped. Its current price is {price_float}"
    )
    send_mail("Price dropped ", message)
