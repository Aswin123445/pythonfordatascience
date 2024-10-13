#the that i am going to create to demonstracte the example of method overriding
class MethodOverriding:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def parent_method(self):
        print(f"this is parent method {self.a + self.b + self.c}")
class ChildClass(MethodOverriding):
    def __init__(self,a,b,c,d):
        super().__init__(a,b,c)
        self.d=d
    #child class overriding the parent method
    def parent_method(self):
        print(f"{self.d}")
#calling the parent method
cl=ChildClass(10,20,30,50)
cl.parent_method()



