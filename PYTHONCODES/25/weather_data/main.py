import csv
from pathlib import Path

temperatures = []
weather_data = []
BASE_DIR = Path(__file__).parent
with open(BASE_DIR / "./weather_data.csv", mode="r") as file:
    data = csv.reader(file)
    weather_data = [row for row in data]
    for row in weather_data[1:]:
        temperatures.append(row[1])
    file.close()
print(temperatures)
print(weather_data)
