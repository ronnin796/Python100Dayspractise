from ntpath import curdir
from bs4 import BeautifulSoup
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

response = requests.get(
    "https://www.empireonline.com/movies/features/best-movies-2/", headers=headers
)
response.raise_for_status()
soup = BeautifulSoup(response.text, "lxml")
movies = soup.find_all(name="strong")[1::]
current_index = 0
movie_list = []
ignore_text = ["Starring:", "Directors:", "Director:"]
movie_titles = [movie.getText() for movie in movies]
for index, value in enumerate(movies):
    if value.get_text() not in ignore_text:
        movie_list.append(value.get_text())

print(movie_list)

with open("movies.txt", mode="a") as file:
    for movie in movie_list:
        file.write(movie + "\n")
