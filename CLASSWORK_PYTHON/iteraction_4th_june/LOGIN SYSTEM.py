print("-----LOGIN SYSTEM-----")

password = "admin123"

while True:

    user = input("Enter Password: ")

    if user == password:
        print("Login Successful.")
        break

    print("Invalid Password.")


## python -u "CLASSWORK_PYTHON/LOGIN SYSTEM.py"