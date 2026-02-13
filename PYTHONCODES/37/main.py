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
from datetime import datetime

today = datetime.now().strftime("%Y%m%d")
pixel_data = {
    "date": today,
    "quantity": "5",
}
try:
    response = requests.post(url=POST_PIXEL_ENDPOINT, json=pixel_data, headers=headers)
    response.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(f"HTTP error occurred: {err}")
except Exception as err:
    print(f"An error occurred: {err}")
print(response.text)

# Update (PUT) the pixel for today
UPDATE_PIXEL_ENDPOINT = f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs/graph1/{today}"
update_data = {
    "quantity": "7",
}
try:
    response = requests.put(
        url=UPDATE_PIXEL_ENDPOINT, json=update_data, headers=headers
    )
    response.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(f"HTTP error occurred (PUT): {err}")
except Exception as err:
    print(f"An error occurred (PUT): {err}")
print("PUT:", response.text)

# Delete the pixel for today
try:
    response = requests.delete(url=UPDATE_PIXEL_ENDPOINT, headers=headers)
    response.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(f"HTTP error occurred (DELETE): {err}")
except Exception as err:
    print(f"An error occurred (DELETE): {err}")
print("DELETE:", response.text)
