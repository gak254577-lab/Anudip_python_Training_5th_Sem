## Problem Statement: Initial Balance = ₹10,000 
# Display a menu repeatedly: 
# 1. Check Balance 
# 2. Deposit 
# 3. Withdraw 
# 4. Exit 
# Requirements: 
# • Withdrawal should not exceed balance.  
# • Display appropriate messages. 
# • Continue until Exit is selected.  



balance = 10000

while True:
    print("\n1.Check Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        print("Balance:", balance)

    elif choice == 2:
        amount = float(input("Enter amount to deposit: "))
        balance += amount
        print("Updated Balance:", balance)

    elif choice == 3:
        amount = float(input("Enter amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print("Remaining Balance:", balance)
        else:
            print("Insufficient Balance")

    elif choice == 4:
        print("Thank You!")
        break

    else:
        print("Invalid Choice")






## python -u "LABWORK_PYTHON/interaction_4th_june_lab/ATM_STIMULATION_SYSTEM.py"