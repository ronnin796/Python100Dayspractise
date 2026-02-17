from bs4 import BeautifulSoup
import requests

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

response = requests.get(url=amazon_url, headers=headers)

soup = BeautifulSoup(response.content, "html.parser")
print(soup.prettify())
# Find the price
price_tag = soup.find("span", class_="a-price-whole")
if price_tag:
    print("Price:", price_tag.get_text())
else:
    print("Price not found. Amazon may be blocking requests.")
