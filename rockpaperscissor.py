from random import randrange as rn

c="y"
while(c=="y"):
    print("1.Rock\n2.Paper\n3.Scissor")
    c=int(input("Enter choice:"))
    g=rn(4)
    if(c==1):
        if g==1:
            print("Rock vs Rock - DRAW!!")
        elif g==2:
            print("Rock vs Paper - computer WINS!!")
        elif g==3:
            print("Rock vs Scissor - user WINS!!")
    elif(c==2):
        if g==1:
            print("Paper vs Rock - user WINS!!")
        elif g==2:
            print("Paper vs Paper - DRAW!!")
        elif g==3:
            print("Paper vs Scissor - computer WINS!!")
    elif(c==3):
        if g==1:
            print("Scissor vs Rock - computer WINS!!")
        elif g==2:
            print("Scissor vs Paper - user WINS!!")
        elif g==3:
            print("Scissor vs Scissor - DRAW!!")
    else:
        print("invalid choice")
    c=input("Do you want to continue(y/n):")
