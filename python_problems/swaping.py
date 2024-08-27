#Write a Python program to swap the values of two variables without using a temporary variable
a=int(input("enter first number"))
b=int(input("enter second number"))
#swapping number using xor

a=a^b
b=a^b
a=a^b
print('the result is {} and {}'.format(a,b),end='\n')

#swapping whit adding technique

a=a+b
b=a-b
a=a-b
print(a," ",b)