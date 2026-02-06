import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).parent

weather_data = pd.read_csv(BASE_DIR / "./weather_data.csv")
temperatures = weather_data["temp"]
print(temperatures)
print(weather_data)
