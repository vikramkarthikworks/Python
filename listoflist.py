gb=[]
s1= ['Vikram', 'A+', 'S', 'A+']
s2= ['Bala','A','S','A+']
gb.append(s1)
gb.append(s2)
print(gb)
ch = input("Do you want to add other student?(y/n)")
while ch == 'y' or ch == 'Y':
    s=[]
    n = input("Enter name:")
    g1 = input("Enter Grade 1:")
    g2= input("Enter Grade 2:")
    g3 = input("Enter Grade 3")
    s.append(n)
    s.append(g1)
    s.append(g2)
    s.append(g3)
    gb.append(s)
    ch = input("Do you want to add other student?(y/n)")
print(gb)

     
