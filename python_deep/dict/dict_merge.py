#Write a Python script to merge two Python dictionaries. 
dic2={3:30, 4:40}
dic3={5:50,1:60}
dic2.update(dic3)
print(dic2)

#Write a Python program to iterate over dictionaries using for loops. 
for x in dic2.keys():
    print(dic2[x])

#Write a Python program to sum all the items in a dictionary.
print(sum(dic2.values()))