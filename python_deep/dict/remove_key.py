#Write a Python program to remove a key from a dictionary.
di={3: 30, 4: 40, 5: 50, 1: 60,10:100}
key=int(input("enter the key you want to delete: "))

#first method
del di[key]
print(di)

#pop method

key=10
print(di.pop(key))

