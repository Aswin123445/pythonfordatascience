# Write a Python program to remove duplicates from a list. 
li=[10,20,30,40,50,10,20,10,10]
print(list(set(li)))

#another way using from key

li=list(dict.fromkeys(li,0))
print(li)