import requests
from decouple import config

client_id = config("MAL_ID")  # Replace with your MAL client ID

url = "https://api.myanimelist.net/v2/anime"
params = {
    "q": "Naruto",
    "limit": 10,
    "offset": 0,
    "fields": "id,title,main_picture,mean",
}

headers = {"X-MAL-CLIENT-ID": client_id}

response = requests.get(url, params=params, headers=headers)

if response.status_code == 200:
    data = response.json()
    for anime in data.get("data", []):
        print(anime["node"]["title"], "-", anime["node"]["mean"])
else:
    print("Error:", response.status_code, response.text)
