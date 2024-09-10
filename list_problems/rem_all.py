list1=[1,2,3,4,2,10,3,52,3,2,2,]
#removing the accurance of the element from the list
#using while loop
number=int(input("enter the numbre"))
while number in list1:
    list1.remove(number)
print(list1)