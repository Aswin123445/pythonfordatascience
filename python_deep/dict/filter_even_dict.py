#Write a Python program to filter even numbers from a dictionary of values
di={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}

#looping method
for i in di:
    di[i]=[x for x in di[i] if x%2!=0]
print(di)

# Write a Python program to convert a dictionary into a list of lists
d={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
#list comprensiation
li=[]
for x,y in d.items():
    li.append([x,y])
print(li)

#list comprensiation method
print([[x,y] for x,y in d.items()])