li=[{'name': 'aswin','age': 19,'place': 'kannur'},{'name': 'arun','age': 30},{'name': 'kalam','age': 25,}]

#list compresiation
li=[i for i in li if len(i) <= 2]
print(li)
i=0
print(li)
while(i<len(li)):
    if len(li[i])>2 :
        del li[i]
    i+=1




    

