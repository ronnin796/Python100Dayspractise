QUARTER = 0.25
DIME = 0.10
NICKLE = 0.05
PENNIES = 0.01
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = {
    "value": 0,
}
def show_resources():
    for key , value in resources.items():
        print(f'{key} = {value} ml')
    print(f'Money = $ {money['value']}')

def check_resources(drink):
    resources_required = drink['ingredients']
    insufficient_ingredients = []
    for key in resources:
        if resources_required.get(key,0)>resources[key]:
            insufficient_ingredients.append(key)
    if not insufficient_ingredients:
        return True
    else:
        format = ", ".join(insufficient_ingredients)
        print('Sorry there is not enough ' , format )
        return False

def calculate_money(quarter,dimes,nickle,pennies):
    return quarter*QUARTER + dimes * DIME + nickle * NICKLE + pennies * PENNIES

def valid_amount(money , drink):
    if money < drink['cost']:
        print('Sorry. You provided Insufficient Money')
        return False
    else:
        return True

def update_resources(drink,amount):
    global resources , money
    resources_drink = drink['ingredients']
    if check_resources(drink) and valid_amount(amount,drink):
        for key in resources:
            resources[key]-=resources_drink.get(key,0)
        money['value']+=drink['cost'] 






while True:
    choice = input('​What would you like? (espresso/latte/cappuccino):').lower()
    if choice == 'resources':
        show_resources()
    elif choice=='stop':
        break
    else:
        drink = MENU[choice]
        if check_resources(drink):
            quarter = float(input('Enter quarters:$ '))
            dimes = float(input('Enter dimes:$ '))
            nickle = float(input('Enter nickle:$ '))
            pennies = float(input('Enter pennies:$ '))

            total_amount = calculate_money(quarter,dimes,nickle,pennies)
            if valid_amount(total_amount,drink):
                update_resources(drink,total_amount)
                print('Enjoy your ', choice)
                print('Heres your change $ ' , round(total_amount-drink['cost'],2))

