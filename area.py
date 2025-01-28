#4. Write a python program to calculate area of circle, rectangle and triangle.

area_of = str(input("Enter the shape : "))

if(area_of == "circle"):
    r = int(input("Enter radius of circle : "))
    circle = 3.14 * r * r
    print("The Area of circle is", circle)

elif(area_of == "rectangle"):
    l = int(input("Enter length : "))
    b = int(input("Enter breath : "))
    rectangle = l * b
    print("The Area of rectangle is", rectangle)

elif(area_of == "triangle"):
    b = int(input("Enter breath : "))
    h = int(input("Enter height : "))
    triangle = 0.5 * b * h
    print("The Area of triangle is", triangle)

else:
    print("Invalid Input")
