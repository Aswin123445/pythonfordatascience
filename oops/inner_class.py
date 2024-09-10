#concept on inner class
class Employee:
    def __init__(self,name,id):
          self.name=name
          self.id=id

    def show(self):
         print(f"name of the employee is {self.name} id of the same is {self.id}")
    
    #creating an inner class
    class Manager:
         def __init__(self,salary,age,):
              self.salary=salary
              self.age=age
            
         def show(self):
              print(f"salary of the manageer is {self.salary} age is {self.age}")

    #creating outer class object
employee=Employee("sharth",1)
employee.show()
manager=employee.Manager(100000,30)
manager.show()