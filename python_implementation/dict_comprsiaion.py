#Square Numbers: Create a dictionary where the keys are numbers from 1 to 10 and the values are their squares.

print({x:x**2 for x in range(1,11)})

di={'aswin':10,'sandeep':30,'ranu':48,'ganesh':12}
#sort the dictionary
print(dict(sorted(di.items(),key=lambda x: x[1],reverse=True)))

#deleting a dictionary 
for x in list(di.keys()):
    if di[x]==12:
        del di[x]
print(di)

# Given a string, create a dictionary that counts the occurrence of each character in the string.
strin='aswin sndeep and they wer all in the dictionary'
print({x:strin.count(x) for x in strin})

#Given a list of words, create a dictionary where the keys are the words
# and the values are True or False depending on whether the word is a palindrome
data=['aswin','ardra','manoj','kumar','rajesh','adcdcda']
print({x: x==x[::-1] for x in data })

#merging two dictionary
dic={1:'aswin',2:'sandeep',3:'rakesh',5:'sandhosh'}
dic52={5:'aswin',2:'sandeep',3:'rakesh',9:'sandhosh'}
print({x:dic.get(x,0)+dic.get(x,0) for x in  set(dic)|set(dic52)})

#shallow copy and deep copy
import copy
a=10
b=copy.copy(a)
print(b)
b=30
print(a)
print(b)

#implementing all concepts of class
class Implement:
    @staticmethod
    def universalmethod():
        print('this is universal method')
    @classmethod
    def classmethods(cls):
        print('this is class method')
    def __init__(self ,a,b):
        self.a=a
        self.b=b
obj=Implement(10,20)
Implement.classmethods()
Implement.universalmethod()

#single inheritance

class SingleInheritance:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        self.sum=0
    def add_sum(self):
        self.sum=self.a+self.b
    @property
    def getter_a(self):
        return self.a
    @getter_a.setter
    def setter_a(self,a):
        self.a=a
#inherited class
class ChildClass(SingleInheritance):
    def __init__(self, a ,b , c ,d):
        super().__init__(a,b)
        self.c=c
        self.d=d

inheriobj=ChildClass(10,20,30,50)
print(inheriobj.getter_a)
inheriobj.setter_a=30
print(inheriobj.getter_a)

#multiple inheritance
class A:
    def helo(self):
        print("helo world")
class B:
    def name(self):
        print("Aswin Sandeep")

#class c will having the property of a and b
class C(A,B):
    def child(self):
        print("child class is called here")
c=C()
c.child()
c.helo()
c.name()

#multilevel inheritance
class GrandParent:
    def metho(self):
        print("this funtion is called from grandparent")
class Parent(GrandParent):
    def method(self):
        print("this funtion is from parent class")
class Child(Parent):
    def child(self):
        print("this funtion is child class")
chi=Child()
chi.metho()


#closure implementation
def outerfuntion(data):
    def innerfuntion():
        return data
    return innerfuntion

data=outerfuntion(4)

print(data())
    
#decorative funtion in python

#example of polymorphism

#polymorphis is the feature in python which object behalf differently on different occasions

#abstraction in python 
from abc import ABC,abstractmethod
class Abstract(ABC):
    @abstractmethod
    def adding_two_numbers(self,a,b):
        pass
        
class Implementaton (Abstract):
    def adding_two_numbers(self, a, b):
        return a+b

a=Implementaton()
print(a.adding_two_numbers(10,30))
