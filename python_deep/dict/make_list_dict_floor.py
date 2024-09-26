#Write a Python program to group the elements of a given list based on the given function.
li=[7, 23, 3.2, 3.3, 8.4]

di={}

for value in li :
    if round(value) in di.keys():
        di[round(value)].append(value)
    else :
        di[round(value)]=[value]
print(di)
