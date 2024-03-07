"""
main.py is the entry point of the coffee machine program. 
It handles user interactions, processes coffee orders, and manages resource levels.
"""
from Function import (insert_coin,
                      resource_used,
                      report,
                      coffee,
                      check_resources)


# from Function import change_counter
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def coffee_machine():
    # TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):"
    choice = input("  What would you like? (espresso/latte/cappuccino):").lower()
    if choice == "off":
        return
    elif choice == "report":
        report()
    elif choice in ["espresso", "latte", "cappuccino"]:
        drink_info = coffee(choice)
        continue_coffee = check_resources(drink_info)
        if continue_coffee == 1:
            print(f"Please insert ${drink_info[3]} in coins.")
            coin_inserted = insert_coin()
            print(f"You have inserted ${coin_inserted}")
            if coin_inserted >= drink_info[3]:
                resource_used(drink_info[0], drink_info[1], drink_info[2], drink_info[3])
                change = coin_inserted - drink_info[3]
                if change > 0:
                    print(f"Here is ${change} in change.")
                print(f"Here is your {choice} ☕. Enjoy!")
            else:
                print("Sorry, that's not enough money. Money refunded.")
    else:
        print("Wrong input provided. Please try again.")
    coffee_machine()


# TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
# TODO: 3. Print report.
# if choice == "report":
# print(report())
# TODO: 4. Check resources sufficient
# remaining_resources = report()
# TODO: 5. Process coins
# total = insert_coin()
# TODO: 6. Check transaction successful
# TODO: 7. Make Coffee
# TODO: 8. Make an option to refill and retract the money.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    # print(f"Your total is: ${total}")
    # print(f"Order cancelled. ${total} being returned.")
    # change_counter(total)
    # print(MENU["espresso"]["ingredients"]["water"])
    coffee_machine()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
