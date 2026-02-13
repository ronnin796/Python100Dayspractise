import requests
from decouple import config
from datetime import datetime, timedelta

SHEET_ENDPOINT = config("SHEETY_API_URL")
SHEET_AUTH_TOKEN = config("SHEETY_HEADER")
HEADERS = {
    "Authorization": SHEET_AUTH_TOKEN,
}


GOOGLE_SHEET_NAME = "Activity Tracker"
root_key = "sheet1"

while True:
    activity = input("Enter activity (or 'exit' to quit): ").strip()
    if activity.lower() == "exit":
        print("Exiting. Goodbye!")
        break
    date_input = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
    if date_input == "":
        date_str = datetime.now().strftime("%Y-%m-%d")
    else:
        date_str = date_input
    time_input = input("Enter time (HH:MM:SS) or press Enter for now: ").strip()
    if time_input == "":
        time_str = datetime.now().strftime("%X")
    else:
        time_str = time_input
    sheet_inputs = {
        root_key: {
            "date": date_str,
            "time": time_str,
            "activity": activity,
        }
    }
    try:
        response = requests.post(url=SHEET_ENDPOINT, json=sheet_inputs, headers=HEADERS)
        response.raise_for_status()
        print(f"Added: {activity} on {date_str} at {time_str}")
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
        print(response.text)
    except Exception as err:
        print(f"An error occurred: {err}")

# After exiting, print all data from the sheet
try:
    response = requests.get(url=SHEET_ENDPOINT, headers=HEADERS)
    response.raise_for_status()
    data = response.json()
    print("\nAll activities in sheet:")
    print(data)
except Exception as err:
    print(f"Could not fetch sheet data: {err}")
