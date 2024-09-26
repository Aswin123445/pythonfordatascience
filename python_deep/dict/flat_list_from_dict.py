#Write a Python program to create a flat list of all the values in a flat dictionary. 

di={'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
#using list compresiation
print([x for x in di.values()])

#Write a Python program to create a flat list of all the keys in a flat dictionary.
print([x for x in di.keys()]) 