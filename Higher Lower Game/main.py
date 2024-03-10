from random import choice
from art import logo, vs
from game_data import data
from replit import clear

def load_char(prev):
    """
    Selects a new character different from the previous one.

    Parameters:
    - prev (dict): The previously chosen character's information.

    Returns:
    - dict: A new character's information.
    """
    char = choice(data)
    if prev['name'] != char['name']:
        return char
    else:
        return load_char(prev)

def description_chart(A, B, score):
    """
    Displays the current game state, including the two characters to compare and the current score.

    Parameters:
    - A (dict): Information about character A.
    - B (dict): Information about character B.
    - score (int): The player's current score.

    Returns:
    - str: The player's guess ('A' or 'B').
    """
    clear()
    print(logo)
    if score > 0:
        print(f"You're right! Current score: {score}")
    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}.")
    print(vs)
    print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}.")
    guess = input("Who has more followers? Type 'A' or 'B': ")
    return guess

def decision_chart(a, b, count):
    """
    Determines if the player's guess is correct and updates the score accordingly.

    Parameters:
    - a (dict): Information about character A.
    - b (dict): Information about character B.
    - count (int): The player's current score.

    Returns:
    - dict or int: The information of the next character if the guess is correct, or 0 if incorrect.
    """
    answer = description_chart(A=a, B=b, score=count).lower()

    if answer == "a":
        user_chosen_count = a["follower_count"]
        if user_chosen_count > b["follower_count"]:
            return a
        else:
            print(f"Sorry, that's wrong. Final score: {count}")
            return 0
    elif answer == "b":
        user_chosen_count = b["follower_count"]
        if user_chosen_count > a["follower_count"]:
            return b
        else:
            print(f"Sorry, that's wrong. Final score: {count}")
            return 0

def HighLow(a, current_score):
    """
    Initiates or continues the HighLow game based on user input.

    Parameters:
    - a (dict): The current character's information.
    - current_score (int): The player's current score.

    Returns:
    None
    """
    game = input("Do you want to play a game of 'Higher or Lower'? \nType 'y' for yes, 'n' for no: ")
    clear()
    if game == "n":
        return
    else:
        b = load_char(a)
        continue_game = decision_chart(a, b, current_score)
        while continue_game != 0:
            a = continue_game
            b = load_char(a)
            current_score += 1
            continue_game = decision_chart(a, b, current_score)
        HighLow(a, 0)


a = choice(data)
count = 0
HighLow(a, count)
