from replit import clear
# HINT: Use clear() to clear the console output.

# Import logo and print it
from art import logo

# Dictionary to store names and bids
bid_dictionary = {}

def highest_bidder(bidding_dictionary):
    """
    Determines the highest bidder from the bidding dictionary.

    Args:
        bidding_dictionary (dict): A dictionary where each key is a bidder's name and each value is their bid amount.

    This function iterates through each item in bidding_dictionary to find the highest bid.
    It prints the name of the highest bidder along with their bid amount.
    """
    highest_bid = 0
    winner = ""
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(logo)
    print(f"The winner is {winner} with a bid of ${highest_bid}.")

# Main loop to ask for user's name and bid
continue_bid = True
while continue_bid:
    print(logo)
    user_name = input("What is your name?: ")
    user_bid = int(input("What is your bid?: $"))
    bid_dictionary[user_name] = user_bid

    more_user = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if more_user == "no":
        continue_bid = False
        clear()
        highest_bidder(bid_dictionary)  # Calls the function to find the highest bidder
    elif more_user == "yes":
        clear()
