import random as rm
stages = [
"""
  +---+
  |   |
      |
      |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
"""
]

words = [
    "apple", "banana", "orange", "grape", "mango",
    "house", "table", "chair", "window", "door",
    "water", "bread", "sugar", "salt", "milk",
    "cat", "dog", "horse", "tiger", "lion",
    "sun", "moon", "star", "cloud", "rain"
]
word_to_guess = rm.choice(words)
print(word_to_guess)
word_length = len(word_to_guess)
player_guess =[""]*word_length
stage_length = len(stages)
lives = len(stages)
print(lives)
word = ""
while(word_to_guess!=word and lives>0):
    guess = input('\nGuess the word: ')
    if guess in word_to_guess:
        if guess in player_guess:
            print("\nAlready Guessed")
        else:
            indices =[i for i , ch in enumerate(word_to_guess) if ch==guess]
            for i in indices:
                player_guess[i]=guess
        print(player_guess)
        for i in range(word_length):
            if player_guess[i]!= "":
                print(player_guess[i], end="" )
            else:
                print("_", end="" )
    else:
        print('Wrong Guess . Try Again')
        lives-=1
    word = ''.join(player_guess)
    print(stages[stage_length-lives-1])

if word == word_to_guess:
    print('\nYou Win !!')
else :
    print('\nYou lose')
print('Word to guess was ' , word_to_guess )
