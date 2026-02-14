import requests
from decouple import config

pixela_endpoint = "https://pixe.la/v1/users"

PIXELA_USERNAME = config("PIXELA_USERNAME")
PIXELA_TOKEN = config("PIXELA_TOKEN")

user_params = {
    "token": PIXELA_TOKEN,
    "username": PIXELA_USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# try:
#     response = requests.post(url=pixela_endpoint, json=user_params)
#     response.raise_for_status()
# except requests.exceptions.HTTPError as err:
#     print(f"HTTP error occurred: {err}")
# except Exception as err:
#     print(f"An error occurred: {err}")
# print(response.text)
graph_endpoint = f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "commit",
    "type": "int",
    "color": "sora",
}
headers = {"X-USER-TOKEN": PIXELA_TOKEN}
# try:
#     response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#     response.raise_for_status()
# except requests.exceptions.HTTPError as err:
#     print(f"HTTP error occurred: {err}")
# except Exception as err:
#     print(f"An error occurred: {err}")
# print(response.text)
POST_PIXEL_ENDPOINT = f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs/graph1"
today = datetime.now().strftime("%Y%m%d")
pixel_data = {

from datetime import datetime

while True:
    user_input = input("Enter what you did today (number of commits or 'exit' to quit): ").strip()
    if user_input.lower() == 'exit':
        print("Exiting. Goodbye!")
        break
    if not user_input.isdigit():
        print("Please enter a valid number or 'exit'.")
        continue
    date_input = input("Enter date (YYYYMMDD) or press Enter for today: ").strip()
    if date_input == '':
        date_str = datetime.now().strftime("%Y%m%d")
    else:
        date_str = date_input
    pixel_data = {
        "date": date_str,
        "quantity": user_input,
    }
    try:
        response = requests.post(url=POST_PIXEL_ENDPOINT, json=pixel_data, headers=headers)
        response.raise_for_status()
        print(f"Pixel added for {date_str}: {user_input}")
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
        print(response.text)
    except Exception as err:
        print(f"An error occurred: {err}")
