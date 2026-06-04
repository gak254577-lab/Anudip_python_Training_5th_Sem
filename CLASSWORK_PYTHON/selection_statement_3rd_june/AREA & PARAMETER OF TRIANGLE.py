## Area and Perimeter of triangle
print("------------------TRIANGLE-------------------")
side1=int(input("Enter the First side of triangle in cm = "))
side2=int(input("Enter the Second side of triangle in cm = "))
side3=int(input("Enter the Third side of triangle in cm  = "))
s=(side1+side2+side3)/2
area=int((s*(s-side1)*(s-side2)*(s-side3))**0.5)
print("Area of triangle is = ",area,"cm**2")
perimeter=side1+side2+side3
print("Perimeter of triangle is = ",perimeter,"cm")


##  python -u "CLASSWORK_PYTHON/AREA & PARAMETER OF TRIANGLE.py"