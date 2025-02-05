#!/usr/bin/python3
# Author: Danny Whitaker
# Date: 2/5/25
# Version 1.0

"""
The goal of this exercise is to complete the scenario:
You work for a pizza delivery company that needs a program to calculate order costs. The company has specific pricing rules:

    Pizza sizes and base prices:
        Small pizza: $8
        Large pizza: $12
    Toppings: $1 for each additional topping
    Delivery fee:
        $2 for the first 5 miles
        $1 for each additional mile

Your task: Create a Python script that prompts the user for order details, calculates the total cost, and displays the result.
"""

# Let's define the pizza prices as a dictionary so that I can not worry about it later.

pizza_prices = {
    "small": 8.00,
    "large": 12.00
}

# Phase 1
# Step 1, lets ask the user for pizza size and validate the input!
pizza_size = input("Please enter pizza size (small or large): ").lower()
# use the .lower to make the response lower case

# failsafe/future-proof
while pizza_size not in pizza_prices:
        print("Invalid Input. Please enter a valid size (small or large)")
        pizza_size = input("Enter pizza size: ")

# Using this below comment to check my progress as I go. Please ignore if reviewing this!
# print(f"You have selected a {pizza_size} pizza which is priced at ${pizza_prices[pizza_size]}.")

# Step 2, lets declare how many toppings and create a failsafe so that it cannot be negative
while True: # I did this before our module on loops, dictionaries, etc; so I had to look up how to create a loop. I apologize if that causes issues
    try:
        num_toppings = int(input("Please enter the number of toppings that you would like: "))
        if num_toppings < 0: # I should leave it at < 0 and not <= incase someone wanted no toppings!
            print("Invalid Input. The number of toppings cannot be negative")
        else:
            break
    except ValueError: # we have to use ValueError if input is not number?
        print("Invalid input. Please enter a valid number of toppings")

# Step 3: let's calculate the delivery distance now
while True:
    try:
        delivery_distance = float(input("Please enter the total distance in miles from the Pizza restaurant: "))
        # by using float(input()) we are making sure that the response is a float/number and not a string!
        if delivery_distance < 0: # lets check if the number is 0 or not
            print("Invalid input. Please give us a real distance to deliver.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Phase 2
# Calculations for Base Prices, toppings, and delivery costs
# Utilize the dictionary that I set above with pizza_prices
base_price = pizza_prices[pizza_size]

# let's calculate the toppings now
topping_costs = num_toppings * 1

# delivery costs
if delivery_distance == 0:
    delivery_fees = 0
elif delivery_distance <= 5: # This is the only place where I found to use elif because I used dictionary for the pizza size.
    delivery_fees = 2
else:
    delivery_fees = 2 + (delivery_distance - 5) * 1 # This should make it for every mile after 5 that the user gets charged $1

# Check if the math is correct using the following print statement in the comment:
# print(f"Your delivery fee is: ${delivery_fees}")
# It works in my testing

# Phase 3
# Computing Total costs
total_cost = base_price + topping_costs + delivery_fees

# Phase 4
# Displaying the final cost to the consumer/user
print(f"Your total order cost for a {pizza_size} pizza with {num_toppings} toppings and delivery distance of {delivery_distance} miles: ${total_cost}")
