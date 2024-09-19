def square(x):
    return x*2
def cube(x):
    return x*2*2

list1=[square,cube]

for li in list1:
    print(li(4))

#opening a file
with open('testint.txt','w') as f:
    f.write('helo world')
with open('testint.txt','r') as f:
   str= f.readline()
   print(str)

a=20
b='str'
print(type(b))
