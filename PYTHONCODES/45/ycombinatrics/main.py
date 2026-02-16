from bs4 import BeautifulSoup
import requests


class News:
    def __init__(self):
        self.response = requests.get("https://news.ycombinator.com/")
        self.soup = BeautifulSoup(self.response.text, "lxml")
        self.news_elements = self.soup.find_all(name="span", class_="titleline")
        self.news_upvotes = self.soup.find_all(name="span", class_="score")
        self.news_link = [news.find("a")["href"] for news in self.news_elements]
        self.news_title = [news.getText() for news in self.news_elements]
        self.news_upvotes = [
            int(news.getText().strip(" points")) for news in self.news_upvotes
        ]

    def get_highest_upvoted_news(self):
        highest_upvoted_news_index = self.news_upvotes.index(max(self.news_upvotes))
        return (
            self.news_title[highest_upvoted_news_index],
            self.news_link[highest_upvoted_news_index],
            self.news_upvotes[highest_upvoted_news_index],
        )

    def print_all_news(self):
        for title, link, upvotes in zip(
            self.news_title, self.news_link, self.news_upvotes
        ):
            print(f"The news is: {title}")
            print(f"The link to the news is: {link}")
            print(f"The upvotes are: {upvotes}")
            print("--------------------------------")


news = News()
TITLE, LINK, UPVOTES = news.get_highest_upvoted_news()
print(f"The most upvoted news is: {TITLE}")
print(f"The link to the news is: {LINK}")
print(f"The upvotes are: {UPVOTES}")
news.print_all_news()
