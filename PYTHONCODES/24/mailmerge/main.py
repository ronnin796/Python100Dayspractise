from pathlib import Path

BASE_DIR = Path(__file__).parent
print(BASE_DIR)
names = []
letter = ""
name_list_file = BASE_DIR / "./Input/Names/invited_names.txt"
letter_file = BASE_DIR / "./Input/Letters/starting_letter.txt"
ready_to_send_letters_path = BASE_DIR / "./Output/ReadyToSend"

# Reading the names
with open(name_list_file, mode="r") as file:
    names = [name.strip() for name in file.readlines()]
    file.close()
# Reading the letter
with open(letter_file, mode="r") as file:
    letter = file.read()
    file.close()

# Generating Letters for each name
for name in names:
    with open(ready_to_send_letters_path / f"letter_for_{name}.txt", mode="w") as file:
        letter_to_send = letter.replace("[name]", name)
        file.write(letter_to_send)


# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
