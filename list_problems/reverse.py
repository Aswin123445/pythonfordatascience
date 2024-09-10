#reverse a list
user_list=[]
flag=True
while flag:
    user_list.append(int(input("enter the number want to add")))
    checker=input("do you want to stop y/n?")
    flag=False if checker=='y' else True
#program to reverse the list
print(user_list)
#temporary reversal
print(list(reversed(user_list)))

#using slicing operation
print(user_list[::-1])

#permanent reversal
user_list.reverse()
print(user_list)

#traditional way
user_list.reverse
for i in range(int(len(user_list)/2)):
    user_list[i],user_list[-1-i]=user_list[-1-i],user_list[i]
print("helo")
print(user_list)