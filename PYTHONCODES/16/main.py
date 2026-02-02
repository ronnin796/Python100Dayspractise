from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from os import system
menu = Menu()
coffee = CoffeeMaker()
money = MoneyMachine()
interface_menu = """
What do you want to do?

1. See available items Menu
2. See Available Resources
3. Get Coffee
4. Exit
"""

while True:
    print(interface_menu)
    ch = int(input('Enter your Choice: '))
    system('clear')
    match ch:
        case 1:
            print(menu.get_items())
        case 2:
            coffee.report()
            money.report()
        case 3:
            print(menu.get_items())
            choice = input('What do you want to get ? :')
            if coffee.is_resource_sufficient(menu.find_drink(choice)):
                if money.make_payment(menu.find_drink(choice).cost):
                    coffee.make_coffee(menu.find_drink(choice))
        case 4:
            break