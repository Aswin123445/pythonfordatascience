#creating a class 
class Methods:
    #init method for initializing the instance varibles

    #class variables
    name='aswin'
    def __init__(self,name,age):
        #making the instance varibles
        self.name=name
        self.age=age

    #creating a access method
    def getter(self):
        return self.name
    
    #creating a mutator method
    def setter(self,age):
        self.age=age

    #making a static method
    #these are the methods that won't make any reference to the class varibles or 
    #reference varibales
    @staticmethod
    def static_funtion():
        print("helo world")

#creating a object of the type 
methods=Methods(age=12,name='aswin')
print(methods.getter())
methods.setter(20)
print(methods.age)

#calling class varibles
print(Methods.name)

#calling the static method
#static methods can ve accessed using class name itself
Methods.static_funtion()
