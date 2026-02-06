import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).parent

squirrel_data = pd.read_csv(BASE_DIR / "./squirrel_data.csv")
# print(squirrel_data)
squirrel_colors = list(set(squirrel_data["Primary Fur Color"].dropna()))

squirrel_count = squirrel_data["Primary Fur Color"].value_counts()
squirrel_count.to_csv(BASE_DIR / "./squirrel_count.csv")
# print(squirrel_count)
data = pd.read_csv(BASE_DIR / "./squirrel_count.csv")
print(data)
