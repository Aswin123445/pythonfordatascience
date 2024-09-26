#Write a Python program to transform a dictionary into a list of tuples. 
di={'Red': 1, 'Green': 3, 'White': 5, 'Black': 2, 'Pink': 4}
print([x for x in di.items()])

#Write a Python program to combine two lists into a dictionary. The elements of the first one serve as keys
#  and the elements of the second one serve as values
keys=['a', 'b', 'c', 'd', 'e', 'f']
valus=[1, 2, 3, 4, 5]
print({x:y for x,y in zip(keys,valus)})