import logging
import requests
from decouple import config
from typing import List, Dict, Optional
from amadeus_connection import AMADEUS


class flightData(AMADEUS):

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
