print("-----PIN VERIFICATION-----")

pin = 3025

while True:

    user = int(input("Enter PIN: "))

    if user == pin:
        print("Access Granted.")
        break

    print("Incorrect PIN. Try Again.")



## python -u "CLASSWORK_PYTHON/PIN VERIFICATION.py"