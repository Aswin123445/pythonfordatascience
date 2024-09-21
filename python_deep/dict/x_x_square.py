#Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x). 

n=int( input("please enter the limit: "))
di={x:x**2 for x in range(1,n+1)}
print(di)

#Write a Python script to print a dictionary where the keys are numbers between 1 and 15
#  (both included) and the values are the square of the keys. 

di1={x:x**2 for x in range(1,16)}
print(di1)
