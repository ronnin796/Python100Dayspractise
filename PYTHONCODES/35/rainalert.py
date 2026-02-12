import requests
from PYTHONCODES.sendmail import send_mail

lat = 27.753129
lon = 85.330416


PARAMS = {
    "lat": f"{lat}",
    "lon": f"{lon}",
    "appid": "f22f75c2f1b17d0019f3c56cc3e50cc9",
    "cnt": "4",
}
try:
    response = requests.get(
        "https://api.openweathermap.org/data/2.5/forecast", params=PARAMS
    )
    response.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(f"HTTP error occurred: {err}")
except Exception as err:
    print(f"An error occurred: {err}")

weather_data = response.json()
weather_forecast = weather_data["list"]
for weather in weather_forecast:
    if weather["weather"][0]["id"] < 700:  # Check for rain conditions
        send_mail(
            subject="Rain Alert",
            body="It's going to rain in the next 12 hours. Don't forget to take an umbrella!",
        )
        break
