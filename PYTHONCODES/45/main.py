from turtle import hideturtle
from bs4 import BeautifulSoup
import requests


class News:
    def __init__(self):
        self.response = requests.get("https://news.ycombinator.com/")
        self.soup = BeautifulSoup(self.response.text, "lxml")
        self.news_elements = self.soup.find_all(name="tr", class_="athing submission")
        self.news_list = self.get_news_list()

    def get_news_list(self):
        self.news_list = [
            {
                "id": news.get("id"),
                "link": news.find("span", class_="titleline").find("a")["href"],
                "title": news.find("span", class_="titleline").getText(),
                "upvotes": self.soup.find(
                    name="span", class_="score", id=f"score_{news.get('id')}"
                ).getText(),
            }
            for news in self.news_elements
        ]
        return self.news_list

    def get_highest_upvoted_news(self):
        highest_upvotes = 0
        highest_upvotes_index = 0
        for index, news in enumerate(self.news_list):
            if int(news["upvotes"].strip(" points")) > highest_upvotes:
                highest_upvotes = int(news["upvotes"].strip(" points"))
                highest_upvotes_index = index
        return self.news_list[highest_upvotes_index]

    def print_news_list(self):
        for news in self.news_list:
            print(news["title"])
            print(news["link"])
            print(news["upvotes"])
            print(news["id"])
            print("--------------------------------")

    def print_highest_upvoted_news(self):
        highest_upvoted_news = self.get_highest_upvoted_news()
        print(f"The most upvoted news is: {highest_upvoted_news['title']}")
        print(f"The link to the news is: {highest_upvoted_news['link']}")
        print(f"The upvotes are: {highest_upvoted_news['upvotes']}")
        print(f"The id is: {highest_upvoted_news['id']}")
        print("--------------------------------")


news = News()
news.print_news_list()
news.print_highest_upvoted_news()
