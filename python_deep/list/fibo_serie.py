#Write a Python program to generate a list containing the Fibonacci sequence, up until the nth term.
limit=int(input("please enter the limit of number"))
#printing fibo
first,second=0,1
for i in range(limit):
    print(first,end=' ')
    first,second=second,second+first