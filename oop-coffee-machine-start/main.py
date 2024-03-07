from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_menu = Menu()
coffee_menu_item = MenuItem
coffee_machine = CoffeeMaker()
coffee_financial = MoneyMachine()


def run_machine():
    get_name = input(f"What would you like to drink? ({coffee_menu.get_items()}): ").lower()
    if get_name == "off":                                               # Check if the user want to turn off the program
        return
    elif get_name == "report":
        coffee_machine.report()                                         # Reports how many resources left
        coffee_financial.report()                                       # Reports how much money is there
    elif coffee_menu.find_drink(get_name):                              # Checks if the drink is in the menu
        selected_drink = coffee_menu.find_drink(get_name)               # Gives a route to the menu
        if (coffee_machine.is_resource_sufficient(selected_drink) and
                coffee_financial.make_payment(selected_drink.cost)):    # Takes money and check if it is enough
            coffee_machine.make_coffee(selected_drink)                  # Deducts the resources and takes the money
    run_machine()                                                       # Recursively runs this program


run_machine()
