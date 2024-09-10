#iterate two list simontenously
list1=[1,2,3,4]
list2=[5,6,7,8]
#iterating list simontenouls 
#for loop
for i,j in zip(list1,list2):
    print(i)
    print(j)

#list comprehensiation
print([ (x,y) for x ,y in zip(list1,list2)])