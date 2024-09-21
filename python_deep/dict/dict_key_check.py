#Write a Python script to check whether a given key already exists in a dictionary. 
a={1: 70, 2: 20, 3: 30, 4: 40, 5: 50}
def is_exist(dict,key):
    if key in dict.keys():
        return True
    return False

print(" key exist " if is_exist(a,10) else "key does not exist" )