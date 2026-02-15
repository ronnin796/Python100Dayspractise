import requests
from decouple import config
from flight_data import flightData
from flight_search import flightSearch
from data_manager import SHEETY
from notification_manager import NotificationManager

notification = NotificationManager()
fs = flightSearch()
sheety = SHEETY()
cities_to_visit = sheety.get_cities()


def main() -> None:
    for city in cities_to_visit:
        city_name = city.get("city")
        iata_code = city.get("iataCode")
        message = ""
        response = fs.search_flight_offers("LON", iata_code, "2024-12-01").get(
            "data", []
        )
        cutoff = city.get("lowestPrice", float("inf"))
        best_price = float("inf")
        print(len(response))
        for offer in response:
            new_price = float(offer.get("price", {}).get("total"))
            if new_price < best_price:
                best_price = new_price
                last_ticketing_date = offer.get("lastTicketingDate")
                flight_id = offer.get("id")
        if best_price <= cutoff:
            message = f"Flight from LON to {city_name} ({iata_code}): Cheapest price: {best_price}, Last ticketing date: {last_ticketing_date}, Flight ID: {flight_id}"
            notification.send_message(message)


if __name__ == "__main__":
    main()
