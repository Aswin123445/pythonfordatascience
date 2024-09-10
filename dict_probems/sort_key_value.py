#square of numbers in dict
print({x:x**2 for x in range(1,11)})

#uppercase mapping
str='aswin'
#mapping
print({c:c.upper() for c in str})

#filter even numbers
numbers=[1,2,3,4,5,6]
print({s:s**2 for s in numbers if s%2==0})

#count the frequency of each character in the string
word='madhu was so frustrated by the use of it'
print({s:word.count(s) for s in word})