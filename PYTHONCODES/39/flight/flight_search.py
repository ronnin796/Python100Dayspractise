import logging
import requests
from decouple import config
from typing import Optional
from datetime import datetime, timedelta


class flightSearch:

    def __init__(self):
        self.api_key = config("AMADEUS_API_KEY")  # from .env
        self.api_secret = config("AMADEUS_API_SECRET")  # from .env
        self.token_url = "https://test.api.amadeus.com/v1/security/oauth2/token"
        self.offer_url = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        self.headers = {"Authorization": f"Bearer {self.get_token()}"}

    def get_token(self) -> Optional[str]:
        data = {
            "grant_type": "client_credentials",
            "client_id": self.api_key,
            "client_secret": self.api_secret,
        }
        try:
            response = requests.post(self.token_url, data=data)
            response.raise_for_status()
            return response.json().get("access_token")
        except requests.RequestException as e:
            logging.error(f"Failed to get Amadeus token: {e}")
            return None

    def search_flight_offers(
        self, origin: str, destination: str, departure_date: str, adults: int = 1
    ) -> dict:
        """Performs a simple flight offer search request."""
        today_date = datetime.now() + timedelta(days=3)
        today = today_date.strftime("%Y-%m-%d")
        params = {
            "originLocationCode": origin,
            "destinationLocationCode": destination,
            "departureDate": today,
            "adults": adults,
            "nonStop": "false",
            "max": 5,
        }
        try:
            response = requests.get(self.offer_url, headers=self.headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logging.error(f"Failed to search flight offers: {e}")
            return {"error": str(e)}
