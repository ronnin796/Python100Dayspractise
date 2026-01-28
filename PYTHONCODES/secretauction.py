import os
print('Welcome to the Auction!!!!!!')

def highest_bidder(bidders):
    highest_bid = 0
    bidder_name = ""
    for key , value in bidders.items():
        if value>highest_bid:
            bidder_name = key
            highest_bid = value
    return bidder_name

while True:
    bidders = {}
    name = input("Enter  your name: ")
    bid = int(input("Enther your bid: $"))
    bidders[name] = bid
    choice = input('Are there any other bidders? (Y or N): ').lower()
    if choice == 'y':
        os.system('clear')
    else:
        break

winner = highest_bidder(bidders)
print('The winner of the auction is ',winner ,'with $',bidders[winner])

