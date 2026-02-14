import requests
from decouple import config

SHEETS_URL = "https://api.sheety.co/d8e303ec42b1dc12b9a759f057939414/flight/sheet1"
AUTHORIZATION_TOKEN = config("FLIGHTS")
print(AUTHORIZATION_TOKEN)
HEADERS = {
    "Authorization": AUTHORIZATION_TOKEN,
}


class DataManager:
    def __init__(
        self,
    ): ...  # This class is responsible for talking to the Google Sheet.
    def get_destination_data(self):
        response = requests.get(url=SHEETS_URL, headers=HEADERS)
        return response.json()

    def fill_iata_codes(self, city, iata_code):
        new_data = {
            "sheet1": {
                "city": city,
                "iataCode": iata_code,
            }
        }
        response = requests.put(
            url=f"{SHEETS_URL}/{city}", json=new_data, headers=HEADERS
        )
        print(response.text)


data_manager = DataManager()
cities_data = data_manager.get_destination_data()["sheet1"]
cities = [data["city"] for data in cities_data]
print(cities)
