#listoperation
lis=[10,20,30,40,50]
lis.append(40)
print(lis)
lis.pop(4)
print(lis)

tup=(39,49,59,9)
print(tup[0])
print(tup.index(39))

a=[10,30,43,54]
b=iter(a)
print(next(b))
print(next(b))

def ye(a :list)->iter:
    yield a
a=ye([10,30,40,50])
nu=iter(next(a))
print(next(nu))
print(next(nu))
print(int('-1'))

#using switch in python
match 5:
    case 1:
        print("helo")
    case 2:
        print("manoj is here")
    case 3:
        print("raghesh also here")
    case 4:
        print("manoj randhish also here")
    case 5:
        print("nalandha university college")
    case _:
        print("invalid entry")

#assert statment in python

for i in [11,30,40,50,33,55]:
    assert i>10,"print this is not a good value"
    
    
    
#exception handling in python
try:
    print("we are inside the except block")
    print("if any error we got in this block will be be redirected to except block")
    c=10/0
except ZeroDivisionError:
    print("excption happend when you try to divide zero")
else :
    print("no errors has been caught you are good")
finally:
    print("its all completed at this point")
    
with open('data.txt','w') as file:
    file.write("this is the begining of the era")
with open('data.txt','r') as file:
    data=file.readline()
    print(data)
import os
os.remove('data.txt')

def outerfuntion(x):
    def innnerfuntion(y):
        return x+y
    return innnerfuntion
x=outerfuntion(5)
print(x(4))
    
#decorator
def decorator(fun):
    #wrapper funtion
    def wrapper():
        print("i am going to make this code pretty")
        fun()
    return wrapper
@decorator
def adding():
    print("this funtion will add two numbers")
adding()


class Proper:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    
    @property
    def get_value_a(self):
        return self.a
    @get_value_a.setter
    def get_value_a(self,a):
        self.a=a
proper=Proper(1,2)
print(proper.get_value_a)
proper.get_value_a=10
print(proper.get_value_a)


