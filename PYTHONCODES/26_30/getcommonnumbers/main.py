from pathlib import Path

BASE_DIR = Path(__file__).parent
squares = [num**2 for num in range(1, 5)]
with open(BASE_DIR / "./file1.txt") as file1:
    file1_numbers = file1.readlines()
    file1_numbers = [int(num.strip()) for num in file1_numbers]
    print(file1_numbers)

with open(BASE_DIR / "./file2.txt") as file2:
    file2_numbers = file2.readlines()
    file2_numbers = [int(num.strip()) for num in file2_numbers]
    print(file2_numbers)

common_numbers = [
    num
    for num in range(max(len(file1_numbers), len(file2_numbers)))
    if num in file1_numbers and num in file2_numbers
]
print(common_numbers)
file1.close()
file2.close()
