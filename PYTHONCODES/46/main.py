from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options

# options = Options()
# options.add_argument("--headless=new")
# # Tell Selenium to use Brave instead of Chrome
# options.binary_location = "/usr/bin/brave-browser"

# driver = webdriver.Chrome(options=options)
# driver.get("https://www.billboard.com/charts/hot-100/")

# songs = driver.find_elements(By.CSS_SELECTOR, "h3#title-of-a-story")

# for song in songs:
#     print(song.text.strip())


#

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from decouple import config

scope = "user-library-read"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=config("SPOTIFY_KEY"),
        client_secret=config("SPOTIFY_SECRET"),
        redirect_uri=config("SPOTIFY_REDIRECT"),
        scope=scope,
        open_browser=False,
    )
)

results = sp.current_user_saved_tracks(limit=50)

for idx, item in enumerate(results["items"], start=1):
    track = item["track"]
    artist = track["artists"][0]["name"]
    name = track["name"]
    print(f"{idx}. {artist} - {name}")
