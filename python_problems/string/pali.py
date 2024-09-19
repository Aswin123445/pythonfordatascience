#checking palidrome
string1=input("enter the string to check it is palidrome or not: ")
string1=string1.lower()
print("it is a palidrome")if string1[::-1]==string1 else print("not a palidrome")