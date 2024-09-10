list1=[1,2,3,4,5,6,7,8,9]
print([ x**2 if x%2==0 else x for x in list1])

a={'a':1,'b':2,'c':3}
b={'a':2,'r':2,'f':3}

c={**a,**b}
for value in c.keys():
    if value in a.keys():
        c[value]+=a[value]
print(c)

#dict compresiation
a={'a':1,'b':2,'c':3}
new_dict={a1:b1 for a1,b1 in a.items() if b1%2!=0 }
print(new_dict)

for a1,b1 in list(a.items()):
    if b1%2==0:
        del a[a1]
print(a)



