#Write a Python program to find the second smallest number in a list.

li=[10,20,2,33,10,50,2,50,33] 
print(sorted(li)[3])


#concatination
sample=['p', 'q']
n =5
li1=[]
for i in range(n):
    for sa in range(len(sample)):
        li1.append(sample[sa]+str(i+1))
print(li1)
        