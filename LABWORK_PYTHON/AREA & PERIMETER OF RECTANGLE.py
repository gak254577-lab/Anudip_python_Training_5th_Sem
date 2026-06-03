print("------ Area and Perimeter of Rectangle ------")
length = float(input("ENTER LENGTH: "))
breadth = float(input("ENTER BREADTH: "))
if length > 0 and breadth > 0:
    area = int(length * breadth)
    perimeter = int(2 * (length + breadth))
    print("Area =", area)
    print("Perimeter =", perimeter)
else:
    print("Invalid Data! Length and Breadth must be positive.")

##   python -u "LABWORK_PYTHON\AREA & PERIMETER OF RECTANGLE.py"