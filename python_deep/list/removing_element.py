#Write a Python program to get a list with n elements
#removed from the left and right.
#Sample Output:
li=[10,20,30,40,50,60]
relement=int(input("enter the size of the element want to remove"))
lor=input("enter the side from which the element you wnat to reomove")
if lor=='right':
    while relement>0:
        li.pop(0)
        relement-=1
else:
    while relement>0:
        li.pop(-1)
        relement-=1
print(li)