a=input("Enter PASSWORD:")
up, lw, sp, dg = 0, 0, 0, 0

if (len(a) < 8):
    print("Password is Weak!")
else:
    for i in range(0, len(a)):
        if (a[i].isupper()):
            up+= 1
        elif (a[i].islower()):
            lw+= 1
        elif (a[i].isdigit()):
            dg+= 1
        else:
            sp+= 1

if (up != 0 and lw != 0 and dg != 0 and sp != 0):
    if (len(a) >= 8):
        print("The strength of password is Strong!.")
    else:
        print("The strength of password is Moderate!.")
else:
    print("invalid password")
