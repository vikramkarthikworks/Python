a=input("password:")
up,lw,nm,sp=0,0,0,0
for i in a:
    if(65 <= ord(i) <= 90):
        up+=1
    elif(97 <= ord(i) <= 122):
        lw+=1
    elif(48 <= ord(i) <= 57):
        nm+=1
    elif(33 <= ord(i) <= 47) or (58 <= ord(i) <= 64) or (91 <= ord(i) <= 96)or (123 <= ord(i) <= 126):
        sp+=1
print(up,lw,nm,sp)
