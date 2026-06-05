## Problem Statement: Accept a number from the user. 
# Display: 
# • Reverse Number  
# • Whether it is a Palindrome  
# Example: 
# Input: 1221 
# Output: 
# Reverse: 1221 
# Palindrome Number 



num = int(input("Enter a number: "))
temp = num
reverse = 0

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

print("Reverse:", reverse)

if reverse == num:
    print("Its a Palindrome Number")
else:
    print("Not a Palindrome Number")




## python -u "LABWORK_PYTHON/interaction_4th_june_lab/PALINDROME_AND_REVERSE_NUMBER_CHECKER.py"