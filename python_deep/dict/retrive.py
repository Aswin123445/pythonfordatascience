#Write a Python program to convert a list of dictionaries into a list 
# of values corresponding to the specified key. 

di=[{'name': 'Theodore', 'age': 18}, {'name': 'Mathew', 'age': 22}, {'name': 'Roxanne', 'age': 20}, {'name': 'David', 'age': 18}]
for x in range(len(di)):
    print(di[x]['age'])
d=[di[x]['age'] for x in range(len(di))]
print({})