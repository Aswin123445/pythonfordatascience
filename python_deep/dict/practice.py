#Write a Python program to count the lowercase letters in a given list of words. 
li=["Red", "Green", "Blue", "White"]
count=0
for i in li:
    for j in range(len(i)):
        if i[j].islower():
            count+=1;
print(count)

#using list comprehensiation
print(sum([i for i in  li for j in i if not j.isupper()]))


