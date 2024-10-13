#this will create a user defined method using class method
class ClassMethod:
    def class_method(cls):
        print("class method is called")
    def __init__(self,id,name,mark):
        self.id=id
        self.name=name
        self.mark=mark
    def printing(self):
        print(f"name is {self.name} id is {self.id} mark is {self.mark}")
a=ClassMethod(id=10,name='aswin',mark=40)
ClassMethod.class_method(ClassMethod)
a.printing()

print(27 and 2)
