#!/usr/bin/env python
# coding: utf-8

# # LAB ASSIGNMENT – Mini Project
# ## AI Number Guessing Game Lite

# In[ ]:


import random

print(" AI Number Guessing Game ")
print("I'm thinking of a number between 1 and 50.")
print("You have 7 attempts to guess it.\n")

secret = random.randint(1, 50)
attempts = 7

while attempts > 0:
    # Ask for guess and validate
    try:
        guess = int(input(f"Guess ({attempts} attempts left): "))
        if guess < 1 or guess > 50:
            print("Please enter a number between 1 and 50.")
            continue
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue
    
    # Check guess
    if guess > secret:
        print("Too high!")
    elif guess < secret:
        print("Too low!")
    else:
        print(f"\nCongratulations! You win in {7 - attempts + 1} attempts! Seems like someone's guessing game is strong :)")
        break
    
    attempts -= 1
    print()
else:
    print(f"\nGame over! The number was {secret}.\n")

print("Thanks for playing!")

