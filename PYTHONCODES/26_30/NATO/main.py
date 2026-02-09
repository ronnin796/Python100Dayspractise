import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).parent


data = pd.read_csv(BASE_DIR / "./nato_phonetic_alphabet.csv")

nato_alphabet = {row.letter: row.code for (index, row) in data.iterrows()}
print(nato_alphabet)
while True:
    word = input("Enter your word: ")
    try:
        word_nato = {letter.upper(): nato_alphabet[letter.upper()] for letter in word}
    except KeyError:
        print("Sorry only letters allowed")
    else:
        print(word_nato)
        break
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
