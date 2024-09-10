class InitMethod:
    def __init__(self,id,location):
       self.id=id
       self.location=location

    #creating a compare funtion
    def compare(self,other):
        return True if self.id==other.id else False

#creating objects
init=InitMethod(1,'kannur')
init2=InitMethod(2,'kerala')
#here the init  method is called by default like 
#so init method wiil acts like a constructor in other programming language

#init method to set the value
class InitMethod1:

    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    #another funtion
    def output(self):
        print(f"name is {self.name} and age is {self.age}")

#creating object
initmethod1=InitMethod1('aswin',22)
initmethod1.output()

print(init.compare(init2))


