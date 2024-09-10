#concat two list based on index base
li1=[1,2,3,4]
li2=[5,6,7,8]
#concatination list comprehensiation
li3=[x+y for x,y in zip(li1,li2)]
print(li3)