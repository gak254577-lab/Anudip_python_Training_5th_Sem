##Problem Statement: Accept a number from the user and determine whether it is a prime number or not. 
# Additional Requirement: If the number is not prime, display all its factors.
# Example: Input: 15 
# Output: Factors: 1 3 5 15 15 is not a Prime Number


n = int(input("Enter a number: "))
is_prime = True
factors = []
if n < 2:
    is_prime = False
else:
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    if len(factors) > 2:
        is_prime = False
if is_prime:
    print(n, "is a Prime Number")
else:
    print("Factors:", *factors)
    print(n, "is not a Prime Number")

## python -u "LABWORK_PYTHON/PRIME_NUMBER.py"