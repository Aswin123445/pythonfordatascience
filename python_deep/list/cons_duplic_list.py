#Write a Python program to remove consecutive
#  (following each other continuously) duplicates (elements) from a given list.
li=[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]

l=len(li)
# for i in range(l-1):
#     if li[i]==li[i+1]:
#         li.pop(i)
#         l-=1


i=0
while i + 1 < l:
    if  li[i]==li[i+1]:
        li.pop(i)
        l-=1
    else:
         i+=1
print(li)

#merging and adding sum for the duplicate

a={'a':1,'b':2,'c':3}
b={'a':4,'d':5,'c':6}

#merging and sorting
a={x:a.get(x,0)+b.get(x,0) for x in set(a)|set(b)}
print(a)

#deleting number from dictionary using del

#sorting based on keys
print(dict(sorted(b.items(),key=lambda x:x[1],reverse= True)))
print(b)

for x in list(a.keys()):
    if a[x]%2==0:
        del a[x]
print(a)


