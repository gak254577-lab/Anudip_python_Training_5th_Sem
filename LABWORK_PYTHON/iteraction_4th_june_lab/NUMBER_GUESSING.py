## Problem Statement: Generate a secret number between 1 and 50. 
## Allow the user to keep guessing until the correct number is found. 
## Display: 
# • "Too High"  
# • "Too Low"  
# • "Correct Guess"  
# Also display the total number of attempts. import random

from random import random
secret = random.randint(1, 50)
attempts = 0
while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess > secret:
        print("Too High")
    elif guess < secret:
        print("Too Low")
    else:
        print("Correct Guess")
        print("Attempts:", attempts)
        break





## python -u "LABWORK_PYTHON/NUMBER_GUESSING.py"