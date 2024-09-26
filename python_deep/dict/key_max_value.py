# Write a Python program to find the key of the maximum value in a dictionary. 
di={'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}
#using dictionary compresiation
max_value=max(list(di.values()))
#accessing the dictionary
for i in di:
    if di[i]==max_value:
        print(i)

#other way to compare the key funtion is
#using the max funtion
print(max(di,key=di.get))