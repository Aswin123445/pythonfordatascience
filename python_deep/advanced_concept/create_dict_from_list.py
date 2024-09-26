#Create a dictionary from two lists: keys = ['a', 'b', 'c'] and values = [1, 2, 3]
keys = ['a', 'b', 'c']
values = [1, 2, 3]
#creating a dictionary from it
di={x:y for x,y in zip(keys,values)}
print(di)