#making two list to dictionary
list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
dict1={}
for x,y in zip(list1,list2):
    dict1[x]=y
print(dict1)

#dict comprehensiation
print({x:y for x,y in zip(list1,list2)})