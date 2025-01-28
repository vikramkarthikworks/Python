#. Write a python program to calculate Body Mass Index (BMI) based on user input.

weight = float(input("Enter your body weight : "))
height = float(input("Enter your body height : "))
bmi = weight / (height ** 2)

if(bmi < 18.5):
    print("You are Underweight")
elif(18.5 <= bmi < 25):
    print("Normal Weight")
elif(25<= bmi < 30):
    print("Overweight")
else:
    print("Obese")
