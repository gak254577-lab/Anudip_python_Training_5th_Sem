## Problem Statement: Accept a number from the user and check whether it is an Armstrong Number. 
# Example: 
# Input: 153 
# Output: 
# 153 is an Armstrong Number 


n = int(input("Enter a number: "))
digits = str(n)
power = len(digits)
total = 0
for d in digits:
    total = total + int(d) ** power
if total == n:
    print(n, "is an Armstrong Number")
else:
    print(n, "is not an Armstrong Number")

## python -u "LABWORK_PYTHON/ARMSTRONG_NUMBER.py"