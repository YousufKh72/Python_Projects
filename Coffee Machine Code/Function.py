from Data import (MENU,
                  Coin_Value,
                  resources)


# change_back ={
#     "Bills": 0,
#     "Quarters": 0,
#     "Dimes": 0,
#     "Nickels": 0,
#     "Cents": 0,
# }


def check_resources(req):
    """
    Checks if sufficient resources are available to make the requested coffee.
    
    :param req: A list with required amounts of water, milk, and coffee.
    :return: 0 if resources are insufficient, otherwise 1.
    """
    if resources["water"] < req[0]:
        print("Sorry. Not enough water.")
        return 0
    elif resources["milk"] < req[1]:
        print("Sorry. Not enough milk.")
        return 0
    elif resources["coffee"] < req[2]:
        print("Sorry. Not enough coffee.")
        return 0
    else:
        return 1


def coin_counter(b, q, d, n, p):
    """
    Calculates the total amount of money inserted by the user based on the quantity of each coin type.

    :param b: Number of one-dollar bills inserted.
    :param q: Number of quarters inserted.
    :param d: Number of dimes inserted.
    :param n: Number of nickels inserted.
    :param p: Number of cents (pennies) inserted.
    :return: The total amount of money inserted as a float.
    """
    bills = b * Coin_Value["bill"]
    quarters = q * Coin_Value["quarter"]
    dimes = d * Coin_Value["dime"]
    nickels = n * Coin_Value["nickel"]
    cents = p * Coin_Value["cent"]
    change = bills + quarters + dimes + nickels + cents
    return change


def insert_coin():
    """
    Prompts the user to input the quantity of each coin type they are inserting into the machine.

    :return: The total amount of money inserted, calculated by calling the coin_counter function.
    """
    b = int(input("How many One Dollar bills?: "))
    q = int(input("How many Quarters?: "))
    d = int(input("How many Dimes?: "))
    n = int(input("How many Nickels?: "))
    c = int(input("How many Cents?: "))
    total = coin_counter(b, q, d, n, c)
    return total


def resource_used(w, m, c, d):
    """
    Deducts the resources used to make a coffee from the machine's available resources.

    :param w: Amount of water used.
    :param m: Amount of milk used.
    :param c: Amount of coffee used.
    :param d: Amount of money to add to the machine's total.
    """
    resources["water"] -= w
    resources["milk"] -= m
    resources["coffee"] -= c
    resources["money"] += d


def report():
    """
    Prints the current resource levels of the coffee machine.
    """
    print(f'Water: {resources["water"]}')
    print(f'Milk: {resources["milk"]}')
    print(f'Coffee: {resources["coffee"]}')
    print(f'Money: ${resources["money"]}')


def coffee(name):
    """ Checks if the input is a coffee or report.
        if it's a coffee uses the resources to make the coffee.
        if it's report, shows current resources left.
        if it's off, it turns off the machine."""
    water_value = MENU[name]["ingredients"]["water"]
    milk_value = MENU[name]["ingredients"].get("milk", 0)
    coffee_value = MENU[name]["ingredients"]["coffee"]
    cost_value = MENU[name]["cost"]
    return [water_value, milk_value, coffee_value, cost_value]

# def change_counter(change):
#     while change != 0:
#         if change >= 1:
#             b = change / 1
#             change = change % b
#             change_back["Bills"] = b
#         elif change >= 0.25:
#             q = change / 0.25
#             change = change % q
#             change_back["Quarters"] = q
#         elif change >= 0.10:
#             d = change / 0.1
#             change = change % d
#             change_back["Dimes"] = d
#         elif change >= 0.05:
#             n = change / 0.05
#             change = change % n
#             change_back["Nickels"] = n
#         else:
#             c = change / 0.01
#             change = change % c
#             change_back["Cents"] = c
#         change_counter(change)
#
# print(f'Returned {change_back["Bills"]} Dollar bills, {change_back["Quarters"]} Quarters, {change_back["Dimes"]}
# Dimes, {change_back["Nickels"]} Nickels, {change_back["Cents"]} Cents')
#
#     change_back["Bills"] = 0
#     change_back["Quarters"] = 0
#     change_back["Dimes"] = 0
#     change_back["Nickels"] = 0
#     change_back["Cents"] = 0
