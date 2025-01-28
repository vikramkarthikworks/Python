#3. Write a python program to calculate simple and compound interest.

mode = str(input("Enter the mode : "))

if(mode == "SI"):
    P = float(input("Enter the principal : "))
    R = float(input("Enter the rate of interest in % per annum : "))
    T = float(input("Enter the time : "))
    Simple_Interest = (P*R*T)/100
    print("The simple interest is", Simple_Interest)

elif(mode=="CI"):
    P = float(input("Enter the principal : "))
    r = float(input("Enter the interest rate: "))
    nT = float(input("Enter the loan time : "))
    Compound_Interest =  P(1 + r/n)^nT-P
    print("The compound interest is", Compound_Interest)
    
else:
    print("Invalid Input")
