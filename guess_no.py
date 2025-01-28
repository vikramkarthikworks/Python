from random import randrange
g=randrange(10)
i=3
while(i>0):
    a=int(input("Guess the Number:"))
    if(a>g):
        print("high! Guess again!")
        i=i-1
    elif(a<g):
        print("low! Guess again!")
        i=i-1
    else:
        print("Congrats You WIN!!")
        break
