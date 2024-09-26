#Write a Python program to select an item randomly from a list. 
import random
list=['aswin','sandeep',10,'madhu',20,40 ,50,'radha']

#randomly pciking a value 
flag=True
while(flag):
    index=random.randint(0,len(list))
    #printing the data
    print(list[index])

    #setting flag
    checker=input("do you want to continue y/n")
    if checker=='n':
        flag=False