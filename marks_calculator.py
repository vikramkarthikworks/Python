def  marks_calculator():
    n = int(input("Total number of subjects:"))
    t = float(input("Tamil:"))
    e = float(input("English:"))
    m = float(input("Maths:"))
    s = float(input("Science:"))
    ss = float(input("Social Science:"))
    total = t + e + m + s + ss 
    print("Total marks acquired:",total)

    average = total/n
    print("Average is:")

    if(average >90):
        print("A")
    elif(90 > average >70):
        print("B")
    elif(70 > average >60):
        print("C")
    elif(60 > average >50):
        print("D")
              
    
marks_calculator()

MALA Y ALAM
