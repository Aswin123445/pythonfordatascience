#finding the common items in two list
list1=[10,20,30,40]
list2=[10,50,60,70]
#using membership operator
for x in list1:
    if x in list2:
        print(f"{x} is common for the both the list")