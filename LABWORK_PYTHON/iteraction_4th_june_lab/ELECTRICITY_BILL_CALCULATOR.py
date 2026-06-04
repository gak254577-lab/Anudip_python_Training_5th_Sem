## Problem Statement: Calculate electricity bill based on the following slab rates: 
# Units  Rate 
# 0-100 ₹5/unit 
# 101-200 ₹7/unit 
# Above 200 ₹10/unit 
# Display: 
# • Units Consumed  
# • Total Bill  
# • Category (Low / Medium / High Consumption)  



import random

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




## python -u "LABWORK_PYTHON/ELECTRICITY_BILL_CALCULATOR.py"