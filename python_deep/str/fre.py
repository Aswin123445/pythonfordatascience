#Write a Python program to count the number of characters (character frequency) in a string
s= 'google.com'

print({x:s.count(x) for x in s})

s1='helo aswin i am coming from the world of science and technology'
s2=[x[::-1] for x in s1.split()]
print(s2)


#first and last character is being swapped 
swapping_string='aswin'
li=list(swapping_string)
li[0],li[-1]=li[-1],li[0]
swapping_string=''.join(li)
print(swapping_string)
print(swapping_string.upper())
print(swapping_string.lower())

#program to remove newline in python

#using spilt and join method
modis=''.join(s1.split())
print(modis)
