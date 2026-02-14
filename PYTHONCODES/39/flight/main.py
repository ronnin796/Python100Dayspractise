# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import logging
from data_manager import SHEETY
from flight_data import AMADEUS


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
