import random
import os

choices = ['Rock' , 'Paper' , 'Scissors']

ascii_arts = {

"Rock" : '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
,
"Paper" : '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
,
"Scissors" : '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
}



print(ascii_arts["Rock"])
def playagain():
    while(True):
        choice = input('Do you want to play again? (y or n)').lower()
        if choice=='y':
            return True
        elif choice == 'n':
            return False
        else:
            print ('Invalid Choice')


while(True):
    os.system('clear')
    while(True):
        playerchoice  = int(input('What do you want to choose? (O:Rock , 1:Paper , 2:Scissors) : '))
        if playerchoice>2:
            print("Invalid Choice!")
        else:
            break
    playerchoice = choices[playerchoice]
    print('You choose ' , playerchoice , "\n" , ascii_arts[playerchoice])
    computerchoice = random.choice(choices)
    print('Computer choose' , computerchoice , "\n" , ascii_arts[computerchoice])

    if playerchoice == computerchoice:
       print('It\'s a draw ')
    elif (playerchoice == "Rock") and (computerchoice == "Paper"):
        print('You loose')
    elif (playerchoice == "Paper") and (computerchoice == "Scissors"):
        print('You loose')
    elif (playerchoice == "Scissors") and (computerchoice == "Rock"):
        print('You loose')
    else:
        print('You win')
    if playagain():
        continue
    else:
        break
    

