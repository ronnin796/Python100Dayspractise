import logging
import requests
from decouple import config
from typing import Optional
from datetime import datetime, timedelta
from amadeus_connection import AMADEUS


class flightSearch(AMADEUS):

    def __init__(self):
        super().__init__()
        self.offer_url = "https://test.api.amadeus.com/v2/shopping/flight-offers"

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
