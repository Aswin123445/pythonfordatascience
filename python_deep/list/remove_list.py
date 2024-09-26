#Write a Python program to print the numbers of a specified list after removing even numbers from it. 
li=[1,23,22,40,80,73,51,48]

#removing even
li=[x for x in li if x%2==0]
print(li)