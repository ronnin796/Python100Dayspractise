import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).parent

weather_data = pd.read_csv(BASE_DIR / "./weather_data.csv")
temperatures_series = weather_data["temp"]
temperatures_list = temperatures_series.to_list()
max_temperature = temperatures_series.max()
average_temperature = sum(temperatures_list) / len(temperatures_list)
print(
    "Average temperature = ",
    round(average_temperature, 2),
    " Max temperature = ",
    max_temperature,
)
# Data in Column
# print(weather_data.day)
# Data in row
# print(weather_data[weather_data.temp == max_temperature])
monday_row = weather_data[weather_data.day == "Monday"]
print(monday_row)
monday_temperature = float(monday_row.temp * 9 / 5 + 32)  # converting int Farenheit
print(monday_temperature)

# Dataframe from scratch
anime_data = {
    "Anime": ["Naruto", "Stiens Gate", "Frieren", "Match Comes in Like a Lion"],
    "Genre": ["Shounen", "Mystery", "Fantasy", "Slice of Life"],
}
anime_dataframe = pd.DataFrame(anime_data)
print(anime_dataframe)
anime_dataframe.to_csv(
    BASE_DIR / "./anime_data.csv"
)  # Converting the dataframe to a csv file
