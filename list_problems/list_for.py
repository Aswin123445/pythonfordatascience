# ['Dear', 'Sir'] should result in ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
list1=['Dear', 'Sir']
list2=['helo','take']
list3=[]
for i in list2:
    for j in list1:
        list3.append(i+' '+j)
print(list3)

#list comprehensiton
list4=[x + ' ' + y for x in list2 for y in list1]
print(list4)
        