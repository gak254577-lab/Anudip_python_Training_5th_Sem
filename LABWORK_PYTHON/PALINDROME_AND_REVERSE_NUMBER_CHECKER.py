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




## python -u "LABWORK_PYTHON/PALINDROME_AND_REVERSE_NUMBER_CHECKER.py"