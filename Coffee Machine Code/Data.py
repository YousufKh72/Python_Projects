"""
Data.py contains the menu configuration and initial resource levels for the coffee machine. 
MENU stores details of each coffee type, including required ingredients and cost.
resources tracks the current availability of water, milk, coffee, and money.
"""
MENU = {
    # Details of available coffee types, including ingredients and costs
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
    # Initial quantities of resources in the coffee machine
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

Coin_Value = {
    # Value of each coin
    "bill": 1,
    "quarter": 0.25,
    "dime": 0.10,
    "nickel": 0.05,
    "cent": 0.01,
}
