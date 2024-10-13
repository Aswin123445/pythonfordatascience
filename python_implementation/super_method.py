#trying to implement super keyword in python
class SuperKeyword:
    def __init__(self,value1,value2):
        self.value1=value1
        self.value2=value2
    def add_two_numbers(self):
        return self.value1 + self.value2
class ChildClass(SuperKeyword):
    def method(cls):
        print("the class method is created")
    def __init__(self,a,b,c,d):
        super().__init__(a,b)
        self.c=c
        self.d=d
    #calling the parent funtion
    def parent(self):
        return super().add_two_numbers()
    def multiply_the_sum(self):
        return self.c * self.d

child = ChildClass(10,20,3,5)
print(child.multiply_the_sum())
#calling the parent funtion
print(child.parent())

#calling the class method
ChildClass.method(ChildClass)
    



