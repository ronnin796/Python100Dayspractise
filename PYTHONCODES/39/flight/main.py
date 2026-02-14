# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

import requests
from decouple import config

data = {
    "grant_type": "client_credentials",
    "client_id": config("AMADEUS_API_KEY"),
    "client_secret": config("AMADEUS_API_SECRET"),
}

token_url = "https://test.api.amadeus.com/v1/security/oauth2/token"
amadeus_url = "https://test.api.amadeus.com/v1/shopping/flight-destinations"
token_response = requests.post(token_url, data=data)
ACCESS_TOKEN = token_response.json().get("access_token")
print(f"Access Token: {ACCESS_TOKEN}")
headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}


# response = requests.get(amadeus_url, params=parameters, headers=headers)
# print(response.json())
parameters = {"keyword": "PARIS", "max": 1}
amadeus_url = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
response = requests.get(amadeus_url, headers=headers, params=parameters)
print(response.json())
