string=input("please enter the word you want to check")
#list comprseiation method
is_palidrome=lambda s: all(s[i]==s[-(i+1)] for i in range(len(s)//2))
print(is_palidrome(string))