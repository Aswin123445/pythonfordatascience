#Write a Python program to check if each number is prime in 
# a given list of numbers. Return True if all numbers are prime otherwise False.

#funtion to check if the string is even or not
def check(li):
     for x in li:
          if x==2:
               continue
          elif x%2==0:
            return False
     return True

#input size from the use
#empty list
li=[]

#input data to the list from the user
i,flag=0,True
while flag:
     li.append(int(input("please enter the value")))
     checker_string=input("do want to stop y/n: ")
     if checker_string=='y':
          flag=False

#printing the list 
print(li)
print(check(li))


