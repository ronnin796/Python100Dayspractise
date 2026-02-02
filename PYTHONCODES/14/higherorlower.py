from art import logo,vs
from game_data import data
import random
from os import system
print(logo)
score = 0
game_over = False
def compare_followers(personA,personB):
    if personA['follower_count']>personB['follower_count']:
        return True
    else:
        return False
compare_A = random.choice(data)
while not game_over:
    print ('Compare A:',compare_A['name'] ,', a ', compare_A['description'],',from ',compare_A['country'] )
    print(compare_A['follower_count'])
    print(vs)
    compare_B = random.choice(data)
    print ('Compare B:',compare_B['name'] ,', a ', compare_B['description'],',from ',compare_B['country'])
    print(compare_B['follower_count'])

    choice = input('Who has higher folloer . A or B: ').lower()
    personA,personB = (compare_A,compare_B) if choice == 'a' else (compare_B,compare_A)


    if compare_followers(personA,personB):
        compare_A = personA
        score += 1
        print('You are Correct. Current Score = ',score)
    else:
        game_over = True
        print('That is wrong. You Lose. Final Score = ',score)  