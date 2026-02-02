import random
attempts = 0
game_end = False

def end_game():
    global game_end
    game_end = True
def update_attemps(difficulty):
    global attempts
    if difficulty == 'easy':
        attempts = 10
    elif difficulty == 'hard':
        attempts = 5
    else:
        print('Wrong Input')
def decreas_attempts():
    global attempts
    attempts -= 1
    if not game_end:
        print('Remaining attempts ',attempts)
def check_guess(target , guess):
    global game_end
    diff = target - guess
    direction = 'left' if (diff<0) else 'right'
    if guess == target:
        end_game()
        print('You win the number to guess was ', target)
    else:    
        if abs(diff)>100:
            print('You are off by  a large number. Make guess to the ' , direction , ' direction')
        elif abs(diff)>20:
            print('You are off by  a medium number.Make guess to the ' , direction , ' direction')
        else:
            print('You are almost close ' , direction , ' direction')
    

while not game_end:
    number_to_guess = random.randint(1,500)
    while not attempts > 0:
        choice = input("Choose your difficulty(easy or hard):").lower()
        update_attemps(choice)

    while not game_end:
        player_guess = int(input('Make your guess: '))
        check_guess(number_to_guess , player_guess)
        decreas_attempts()
        if attempts == 0:
            end_game()
            print('Out of attempts . You Lose . The number to be guessed was ' , number_to_guess ,'.')
            break

