#Write a Python program to create a dictionary
#  with the same keys as the given dictionary and values generated by running the given function for each value.
di= {'Theodore': {'user': 'Theodore', 'age': 45}, 'Roxanne': {'user': 'Roxanne', 'age': 15}, 'Mathew': {'user': 'Mathew', 'age': 21}}
#3162
#using dictionary compresiation
d={x:di[x]['age'] for x in di}
print(d)

#Write a Python program to convert a list of dictionaries into a list
#  of values corresponding to the specified key.Sample Output:

li=[{'name': 'Theodore', 'age': 18}, {'name': 'Mathew', 'age': 22}, {'name': 'Roxanne', 'age': 20}, {'name': 'David', 'age': 18}]

#using list comprsiation
print([li[x]['age'] for x in range(len(li))])