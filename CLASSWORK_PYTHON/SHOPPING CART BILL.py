print("-----SHOPPING CART-----")

total = 0

while True:

    price = int(input("Enter Item Price: "))

    if price == 0:
        break

    total = total + price

print("Total Bill Amount:", total)




## python -u "CLASSWORK_PYTHON/SHOPPING CART BILL.py"