#Write a Python program to replace the last element in a list with another list.
realli=[1, 3, 5, 7, 9, 10]
replacer=[2, 4, 6, 8]

realli[-1]=replacer
print(realli)

#Write a Python program to insert a given string at the beginning of all items in a list. 
li= [1,2,3,4]
st= 'emp'
for i in range(len(li)):
    li[i]=str(i+1)+st
print(li)
