#Write a Python program to find all keys in a dictionary that have the given value
di={'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}

value=int(input("please enter the value want to find the key: "))
for i in di:
    if di[i]==value:
        print(i)
