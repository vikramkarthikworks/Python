'''
Write a Python program to create a Caesar cipher encryption and display input text,
encrypted text and decrypted text.

Basic Operations:
• Creating a List: Use [ ] and comma-separated values.
• Accessing Elements: Indexing starts at 0; use slicing for subsets.
• Modifying Elements: Direct assignment or methods like append(),
insert(), extend().
• Removing Elements: del statement, remove(), pop()
• Iterating through a List: Use loops like for or list comprehensions.
• List Methods: Familiarize with common methods such as sort(),
reverse(), count(), etc.,
• List Comprehensions: Efficiently create lists based on conditions.
Eg: without list
Text = input("Text:")
empty = ""


'''
#code
a = str(input("Text:"))
list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
l = []
e=''
k = int(input('key:'))
for i in a:
    l.append(i)
for i in l:
    for j in list:
        if i==j:
            l[l.index(i)] = list[(list.index(j)+k)%26]
for i in l:
    e = e+i
print("Encrypted text:",e)
print("Decrypted text:",a)




















