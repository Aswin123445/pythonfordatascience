#Find all of the numbers from 1-1000 that are divisible by 7
print([i for i in range(1,1001) if i%7==0])

#Count the number of spaces in a string
string='aswin sandeep from'
print(sum([1 for char in string  if char==' ']))