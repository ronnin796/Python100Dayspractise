import requests
from decouple import config
from flight_data import flightData
from flight_search import flightSearch
from data_manager import SHEETY

fs = flightSearch()
sheety = SHEETY()
cities_to_visit = sheety.get_cities()
print(cities_to_visit)
# print(cities_to_visit)
# for city in cities_to_visit:
#     city_name = city.get("city")
#     iata_code = city.get("iataCode")
#     print(f"{city_name}: {iata_code}")

# for city in cities_to_visit:
#     city_name = city.get("city")
#     iata_code = city.get("iataCode")
#     response = fs.search_flight_offers("LON", iata_code, "2024-12-01").get("data", [])
#     price = 1000
#     print(len(response))
#     for offer in response:
#         new_price = float(offer.get("price", {}).get("total"))
#         if new_price < price:
#             price = new_price
#             print(price)
#             last_ticketing_date = offer.get("lastTicketingDate")
#             flight_id = offer.get("id")

#     print(
#         f"Flight from LON to {city_name} ({iata_code}): Cheapest price: {price}, Last ticketing date: {last_ticketing_date}, Flight ID: {flight_id}"
#     )
