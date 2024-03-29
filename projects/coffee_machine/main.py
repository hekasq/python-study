from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


def parse_input(input):
    if input == 'off':
        exit()
    elif input == 'report':
        coffee_maker.report()
        money_machine.report()
        return None
    else:
        return menu.find_drink(input)


def run():
    while True:
        response = input("What would you like? (espresso, latte, cappuccino)")

        drink = parse_input(response)
        if drink is None:
            continue
        if not coffee_maker.is_resource_sufficient(drink):
            continue
        payment_successful = money_machine.make_payment(drink.cost)
        if (payment_successful):
            coffee_maker.make_coffee(drink)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run()
