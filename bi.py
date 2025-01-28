h=float(input("Height:"))
w=float(input("Weight:"))
bmi=w/(h**2)
if(bmi>18.5):
    print('Underweight')
elif(18.5<=bmi):
    if(bmi < 25):
        print('Normal Weight')
    else:
        if(bmi < 30):
            print('Overweight')
else:
    print("obese")
