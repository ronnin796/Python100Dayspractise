import requests
from decouple import config
from flight_data import flightData
from flight_search import flightSearch
from data_manager import SHEETY

fs = flightSearch()
sheety = SHEETY()
cities_to_visit = sheety.get_cities()
print(cities_to_visit)
response = sheety.get_users()
print(response)
