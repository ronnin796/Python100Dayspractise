import requests
from datetime import datetime
from config import send_notification

MY_LAT = 28.555429
MY_LNG = -75.850670

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# Your position is within +5 or -5 degrees of the ISS position.
import math


def angular_distance(lat1, lon1, lat2, lon2):
    # Convert to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    # Spherical law of cosines
    angle = math.acos(
        math.sin(lat1) * math.sin(lat2)
        + math.cos(lat1) * math.cos(lat2) * math.cos(lon2 - lon1)
    )

    # Convert back to degrees
    return math.degrees(angle)


def is_within_5_degrees(my_lat, my_lon, iss_lat, iss_lon):
    distance_deg = angular_distance(my_lat, my_lon, iss_lat, iss_lon)
    return distance_deg <= 5


parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
time_now_hour = time_now.hour
print(f"Current Hour: {time_now_hour}")
print(f"Sunrise Hour: {sunrise}")
print(f"Sunset Hour: {sunset}")
if is_within_5_degrees(MY_LAT, MY_LNG, iss_latitude, iss_longitude) and (
    time_now_hour >= sunset or time_now_hour <= sunrise
):
    send_notification()
else:
    print("ISS is not overhead or it's not dark yet.")
# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
