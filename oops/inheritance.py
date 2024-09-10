#inheritance is the property of accuring the behafioour or
#charateristics of one class to other class

#single level inheritance
class Parent:
    def __init__(self,age,name):
        self.age=age
        self.name=name
    def show(self):
        print(f"helo world{self.age} {self.name}")
class Child(Parent):
    def __init__(self, age, name):
        super().__init__(age, name)
    def child(self):
        print("how are you")

#creating object
objec=Child()
objec.show()
objec.child()