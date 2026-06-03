angle1=int(input("Enter the first angle of the triangle: "))
if angle1<=0:
    print(" Angles1 must be positive.")
    exit()
angle2=int(input("Enter the second angle of the triangle: "))
if angle2<=0:
    print(" Angles2 must be positive.")
    exit()
angle3=int(input("Enter the third angle of the triangle: "))
if angle3<=0:
    print(" Angles3 must be positive.")
    exit()
if angle1 + angle2 + angle3 == 180:
    print("\n-------The angles form a triangle.-------")
else:
    print("\n-------The angles do not form a triangle.-------")