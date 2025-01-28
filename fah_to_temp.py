#2. Write a python program to convert Fahrenheit to Celsius and vice versa.

F = float(input("Enter the Fahrenheit : "))
C = (F - 32) * 5/9
print("The Celcius : ",C )


C = float(input("Enter the Celcius : "))
F = (C * 9/5) + 32
print("The Fahrenheit : ",F )
