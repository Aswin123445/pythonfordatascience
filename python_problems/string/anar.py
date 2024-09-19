#non-pythonic way to check the string is anorghous or not
str1=input("enter string: ")
str2=input("enter string: ")
flag=True
for s in str1:
    if s not in str2:
       flag=False
       break
if flag==False:
    print("it is not anargham")
else :
    print("String is an anargham")

#pythonic way is to check using the consept of set
print("is anagolic") if set(str1)==set(str2) else print("not arnoligic")
