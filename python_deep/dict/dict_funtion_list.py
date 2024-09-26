#Write a Python program to map the values of a given list to a dictionary using a 
#function, where the key-value pairs consist of the original value as the key and the result of the function as the value.
key=[1,2,3,4,5,6,7,8]
d={}
#funtion to convert the given key into square
def to_square(value):
    return value**2

#making dicitionay

print({x:to_square(x) for x in key})

#without using dict compresiation
for i in key:
    d[i]=to_square(i)
print(d)