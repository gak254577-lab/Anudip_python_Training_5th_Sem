print("-----GUESS THE NUMBER-----")

secret = 7

while True:

    guess = int(input("Guess the Number: "))

    if guess == secret:
        print("Congratulations! You guessed the correct number.")
        break

    print("Wrong Guess. Try Again.")


## python -u "CLASSWORK_PYTHON/GUESS THE NUMBER GAME.py"