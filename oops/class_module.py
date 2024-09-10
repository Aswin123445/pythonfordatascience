#creating a module for multiple class
class MyCustomError(Exception):
    pass
class Operations:
    """class to perform mathamatical opeations"""
    def __init__(self,number1,number2):
        self.number1=number1
        self.number2=number2
    
    def sum(self):
        """method to find the sum of two number and return the result to the user"""
        result=self.number1+self.number2
        return result
    
    def sub(self):
        """method to find the subsraction  of two number and return the result to the user"""
        try:
            if(self.number1>self.number2):
                result=self.number1-self.number2
                return result
            else :
                raise MyCustomError('value shold be greater than the first one')
        except MyCustomError as e:
            print(e)
    
class PrintName:
    """this class is used to print the name of the user"""
    def __init__(self,name):
        self.name=name
    def print_name(self):
        print(f"helo the user name is {self.name}")
    