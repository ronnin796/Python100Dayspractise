import logging
import requests
from decouple import config
from typing import List, Dict, Optional


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
