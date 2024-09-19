class Fact:
    def __init__(self,fact):
        self.__fact=fact
    
    @property
    def getter(self):
        return self.__fact
    @getter.setter
    def getter(self,value):
        self.__fact=value
    
    def factorial(self,data):
        if data<1:
            return 1
        else:
            return self.factorial(data-1)*data
    def fact_normal(self,data):
        product=1
        while(data>0):
            product*=data
            data-=1
        return product
fact=Fact(5)
print(fact.factorial(5))
print(fact.fact_normal(5))


