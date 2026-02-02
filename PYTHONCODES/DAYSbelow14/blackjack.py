import random
cards = [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10,10,10,10]
dealer=[]
player=[]
turn = 0
player_stand = False
dealer_stand  = False
def check_points(cards_list):
    points = sum(cards_list)
    ace = 0
    for card in cards_list:
        if card == 1:
            ace += 1
    
    if ace > 0 and points+10<=21:
        points += 10
    return points

print("Lets get started with black jack!!!")
for i in range(2):
    dealer.append(random.choice(cards))
    player.append(random.choice(cards))

while not (player_stand and dealer_stand):
    print('The dealer has ',end="" )
    for i in range(turn+1):
        if i<len(dealer):
            print(dealer[i] , " " , end="")
        else:
            pass
    print('\nYou have',player)
    if check_points(player)==21:
            print("Player wins " , player )
            break
    while player_stand == False :
        if check_points(player)>21:
            break
        choice = int(input("Do you want to hit or stand(0:Hit 1:Stand) :"))
        
        match choice:
            case 0:
                player.append(random.choice(cards))
                print('\nYou have',player)
                
            case 1:
                player_stand = True
            case _:
                pass
    if check_points(player)>21:
        print('You Bust! You lose')
        print('You have',player)
        break
    
    
    
    if (check_points(dealer)<17) and not dealer_stand:
        print('Dealer Hits:')
        dealer.append(random.choice(cards))
        if check_points(dealer)>21:
            print('Dealer Bust!! You Winn')
            break
        if check_points(dealer)>=17:
            print('Dealer Stands:')
            dealer_stand = True  
    if check_points(dealer)>21:
        print('Dealer Bust!! You Winn')
        break 
    turn+=1 
    
print('Dealer has ' , dealer , 'Player has ' , player)
if player_stand and dealer_stand:
    if check_points(player)>check_points(dealer):
        print('Player Wins')
    elif check_points(player)==check_points(dealer):
        print('Draw')
    else:
        print('Dealer wins')