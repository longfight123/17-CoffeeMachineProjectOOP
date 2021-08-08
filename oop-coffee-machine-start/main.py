from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker_object = CoffeeMaker()
money_machine_object = MoneyMachine()


def make_a_drink():

    a_menu_object = Menu()
    print(a_menu_object.get_items())
    user_drink = input('What would you like?')
    if user_drink == 'report':
        coffee_maker_object.report()
        money_machine_object.report()
        make_a_drink()
    elif user_drink == 'off':
        return
    user_drink = a_menu_object.find_drink(user_drink)
    if not user_drink:
        make_a_drink()
    if coffee_maker_object.is_resource_sufficient(user_drink):
        print(f'Please make payment, the cost of your drink is {user_drink.cost}:')
        if money_machine_object.make_payment(user_drink.cost):
            coffee_maker_object.make_coffee(user_drink)
            make_a_drink()
        else:
            make_a_drink()
    make_a_drink()


make_a_drink()

