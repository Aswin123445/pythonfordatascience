list1=[10,20,30,40,60]
list2=[100,200,301]
dict2={x:y for x,y in zip(list1,list2)}
print(dict2)

#merge two python dictionary to one
dict1={10:200,'b':200,'c':401}
dict1.update(dict2)
print(dict1)

#deleting a dictionary if value is dividable by 2

dict3={x:y for x,y in dict1.items()  if y%2!=0}
print(dict3)

for x in list(dict1.keys()):
    if dict1[x]%2==0:
        del dict1[x]
print(dict1)

#merge two dictionary
dict3={**dict1,**dict2}
dict4=dict1|dict2

print(dict3  ,dict4)

#merging two dictionary and adding the sum of the dictionary
d1={'a':10,'b':20,'c':30}
d2={'c':100,'b':200,'d':300}
for x in d1.keys():
    if x in d2.keys():
        d1[x]+=d2.pop(x)
print(d1|d2)
d5={'c':100,'b':200,'d':300}
#find the interesection of two dictionary
intersection={key:d1[key] for key in d1.keys() if key in d5.keys()}
print(intersection)
print(d5)
print(d5.keys())


#remove duplicates value from the dictionary

dict5={1:'aswin',2:'sandeep',3:'arun',4:'aswin'}
#dict compresiation
ch=set()
for key,value in  list(dict5.items()):
    if value in ch:
        del dict5[key]
    else:
        ch.add(value)
print(dict5)
        










