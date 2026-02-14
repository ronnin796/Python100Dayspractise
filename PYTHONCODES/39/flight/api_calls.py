import logging
from typing import List, Dict, Optional
import requests
from decouple import config


class SHEETY:
    """Handles interactions with the Sheety API for city and IATA code management."""

    def __init__(self) -> None:
        self.SHEETS_URL = config("SHEETY_FLIGHT_URL")
        self.AUTHORIZATION_TOKEN = config("FLIGHTS")
        self.HEADERS = {"Authorization": self.AUTHORIZATION_TOKEN}

    def get_cities(self) -> List[Dict]:
        """Fetches the list of cities from the Sheety API."""
        try:
            response = requests.get(url=self.SHEETS_URL, headers=self.HEADERS)
            response.raise_for_status()
            return response.json().get("sheet1", [])
        except requests.RequestException as e:
            logging.error(f"Failed to fetch cities: {e}")
            return []

    def update_iata_code(self, city_id: int, iata_code: str) -> None:
        """Updates the IATA code for a specific city in the Sheety API."""
        update_url = f"{self.SHEETS_URL}/{city_id}"
        body = {"sheet1": {"iataCode": iata_code}}
        try:
            response = requests.put(url=update_url, json=body, headers=self.HEADERS)
            response.raise_for_status()
            logging.info(f"Updated city ID {city_id} with IATA code {iata_code}.")
        except requests.RequestException as e:
            logging.error(f"Failed to update IATA code for city ID {city_id}: {e}")

    def update_all_iata_codes(self, cities: List[Dict], amadeus: "AMADEUS") -> None:
        """Updates IATA codes for all cities using the Amadeus API."""
        for city in cities:
            city_name = city.get("city")
            city_id = city.get("id")
            if not city_name or not city_id:
                logging.warning(f"Missing city name or ID in city data: {city}")
                continue
            iata_code = amadeus.get_iata_code(city_name)
            if iata_code:
                self.update_iata_code(city_id, iata_code)
            else:
                logging.warning(f"No IATA code found for city: {city_name}")


class AMADEUS:
    """Handles authentication and city IATA code lookup via the Amadeus API."""

    def __init__(self) -> None:
        self.data = {
            "grant_type": "client_credentials",
            "client_id": config("AMADEUS_API_KEY"),
            "client_secret": config("AMADEUS_API_SECRET"),
        }
        self.token_url = "https://test.api.amadeus.com/v1/security/oauth2/token"
        self.amadeus_url = (
            "https://test.api.amadeus.com/v1/reference-data/locations/cities"
        )
        self.headers = {"Authorization": f"Bearer {self.get_token()}"}

    def get_token(self) -> Optional[str]:
        """Retrieves an access token from the Amadeus API."""
        try:
            response = requests.post(self.token_url, data=self.data)
            response.raise_for_status()
            return response.json().get("access_token")
        except requests.RequestException as e:
            logging.error(f"Failed to get Amadeus token: {e}")
            return None

    def get_iata_code(self, city: str, country_code: str = "NP") -> Optional[str]:
        """Fetches the IATA code for a given city name and country code."""
        parameters = {"keyword": city, "max": 1, "countryCode": country_code}
        try:
            response = requests.get(
                self.amadeus_url, headers=self.headers, params=parameters
            )
            response.raise_for_status()
            data = response.json().get("data", [])
            if data and "iataCode" in data[0]:
                return data[0]["iataCode"]
            logging.warning(f"No IATA code found in Amadeus response for city: {city}")
            return None
        except requests.RequestException as e:
            logging.error(f"Failed to fetch IATA code for {city}: {e}")
            return None


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    sheets = SHEETY()
    amadeus = AMADEUS()
    cities = sheets.get_cities()
    if not cities:
        logging.error("No cities found to update.")
        return
    logging.info(f"Fetched {len(cities)} cities from Sheety.")
    sheets.update_all_iata_codes(cities, amadeus)


if __name__ == "__main__":
    main()
