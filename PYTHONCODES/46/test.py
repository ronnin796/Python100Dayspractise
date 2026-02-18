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
SPOTIFY_ID = config("SPOTIFY_KEY")
SPOTIFY_SECRET = config("SPOTIFY_SECRET")
REDIRECT_URL = config("SPOTIFY_REDIRECT")
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIFY_ID,
        client_secret=SPOTIFY_SECRET,
        redirect_uri=REDIRECT_URL,
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

user_id = sp.current_user()["id"]

playlist = sp.user_playlist_create(
    user=user_id, name="My Billboard Playlist", public=False
)

print("Playlist created:", playlist["external_urls"]["spotify"])
