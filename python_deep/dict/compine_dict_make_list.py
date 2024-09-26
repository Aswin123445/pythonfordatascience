# Write a Python program to find the specified number of maximum 
# values in a given dictionary.Original Dictionary:
li={'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}
#input number of maxiumu values to find
count=int(input("enter the maximum values"))
for x in range(count):
    print(li[max(li,key=li.get)]) 
    del li[max(li,key=li.get)]

