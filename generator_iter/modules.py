from random import randint
print(randint(1,40))

#generate otp numbers
flag=True
while flag:
    print(randint(100_000,999_999))
    inpt=input("do you want to stop ?y/n")
    flag=False if inpt=='y' else True

str1="aswin sandeep helo how are you doing"
print(str1.split())