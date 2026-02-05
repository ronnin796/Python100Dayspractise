from pathlib import Path


BASE_DIR = Path(__file__).parent


my_folder = BASE_DIR / "my_folder"
file_name = BASE_DIR / "my_file.txt"


with open(file_name, mode="w") as file:
    file.write("Gyapan is pepega lol lmafo even ")
