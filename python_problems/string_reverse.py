string=input("enter a stirng")
st=''
for i in range(len(string)):
    st+=string[-1-i]
print("reversed string is ",st)

#pythonic way
st=string[::-1]
print(st)

