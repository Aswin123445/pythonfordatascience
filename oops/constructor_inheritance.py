#in this multilevel inheritance and we do the conept on construntor in it

#parent class
class parent:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(f"parent called{self.name} {self.age}")
    
    def helo():
        print("parent helo")

#child class
class child(parent):
    def __init__(self,name,age,p_name,p_age):
        super().__init__(p_name,p_age)
        self.name=name
        self.age=age
        print(f"child called {self.name,self.age} ")
    
    def helo():
        print("child helo")

ch=child('aswin',12,'arun',40)