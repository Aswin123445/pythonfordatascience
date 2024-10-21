print([x**2 for x in range(1,11)])
print(''.join([x.upper() for j in 'aswin sandeep and team'.strip() for x in j]))
#generate list of prime numbers from 50
def is_prime(number):
    if number==2:
        return True
    i=2
    while(i<number):
        if(number%i==0):
            return False
        else :
            i+=1
    return True
print([x for x in range(2,50) if is_prime(x)])

#List the number of characters in each word from a sentence
word='aswin sandeep and co workers in the field of technology'
print([len(x) for x in  word.split() if len(x) %2 ==0])

#String Reversal: Reverse each word in a given list of words.
word2='aswin sandeep and co workers in the field of technology'
print([x[::-1] for x in  word2.split()])

#Sum of Digits: Create a list of the sum of digits for numbers from 1 to 20.
print(sum([x for x in range(1,21)]))

#Write a Python program that checks whether a number is positive, negative, or zero using an if-elif-else condition.
print(['positive' if x > 0 else 'negative' if x<0 else 'zero' for x in [10,-23,3,0,43,-22]])

print([[1 for i in range(1,4)] for j in range(1,4)])

#list of vowels
print([x for x in word if x in ('a','e','i','o','u')])

#Create a list of numbers from 1 to 100 that are divisible 
# by both 2 and 3 using a nested list comprehension with an if condition.
print([x for x in range(3,101,3) if x%2 == 0])

lis = [[1, -2, 3], [-4, 5], [6, -7, 8]]

print([x for j in lis  for x in j  if x >0])


