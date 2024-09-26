#find the second largest element in the dictionary
a=[10,30,40,50,34]
lar=0
seclar=0
for x in range(len(a)):
    if(x==0):
        lar=seclar=a[x]
    else:
        if a[x]>lar:
            seclar=lar
            lar=a[x]
print(seclar)
print(lar)