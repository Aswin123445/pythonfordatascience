#we need to string to containation
string1,string2=input("enter two string seprated by space").split()
#concatination
len=len(string1)
for i in range(len(string2)):
    string1[len+i+1]=string2[i]
print (string1)