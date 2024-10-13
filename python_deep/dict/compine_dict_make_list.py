# Write a Python program to find the specified number of maximum 
# values in a given dictionary.Original Dictionary:
li={'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}
#input number of maxiumu values to find
count=int(input("enter the maximum values"))
for x in range(count):
    print(li[max(li,key=li.get)]) 
    del li[max(li,key=li.get)]


#merging two dictioanry and finding the sum of the common value
d1={'a':10,'b':20,'c':30}
d2={'a':30,'b':20,'c':30}
#using dict compresiation
print( {x : d1.get( x , 0 ) + d2.get( x , 0) for x in  set(d1) | set(d2)} )

#using a regular for loop

for x,y in d1.items():
    if x in d2:
        d1[x]+=d2[x]
print(d1)

#finding the key with maximum value

print(d1[max(d1,key=d1.get)])


