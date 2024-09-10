string=input("enter the string want to make the operarions")
uniset={char for char in string}

#finding the count in the chararteres
dict1={}
for uni in uniset:
    count=string.count(uni)
    dict1[uni]=count
print (dict1)
