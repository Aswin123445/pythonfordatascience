#Merge two dictionaries: dict1 = {'a': 1, 'b': 2} and dict2 = {'c': 3, 'd': 4}.
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

dict1={**dict1,**dict2}
print(dict1)