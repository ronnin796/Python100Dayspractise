from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
soup = BeautifulSoup(response.text, "lxml")
# print(soup.prettify())
titles = soup.find_all(name="span", class_="titleline")
for title in titles:
    print(title.getText(), " link :", title.find("a")["href"])
