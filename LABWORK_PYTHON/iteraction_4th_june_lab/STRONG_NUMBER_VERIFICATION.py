## Problem Statement: A Strong Number is a number whose sum of factorials of digits equals the number itself. 
# Write a program to check whether a given number is a Strong Number. 
# Example: 
# Input: 145 
# Output: 
# 145 is a Strong Number 


import math

num = int(input("Enter a number: "))
temp = num
sum_fact = 0

while temp > 0:
    digit = temp % 10
    sum_fact += math.factorial(digit)
    temp //= 10

if sum_fact == num:
    print(num, "is a Strong Number")
else:
    print(num, "is not a Strong Number")





## python -u "LABWORK_PYTHON/STRONG_NUMBER_VERIFICATION.py" 