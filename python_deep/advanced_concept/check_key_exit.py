#check a key exist in a table
di={'a':10,'b':20,'c':30,'d':40}

#inputing a key from the user
key=input("please enter the key: ")

#checking the key in the database or not
if key in di.keys():
    print("key exist in the database")

#Update the value of a key in a dictionary.
if key in di.keys():
    di[key]=100
print(di)

#Remove a key from a dictionary.

di.pop(key)
print(di)

