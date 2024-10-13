class Duder:
    def __init__(self,value: int)->int:
        self.value = value
    def __mul__(self,other):
        return self.value + other.value
obj=Duder(4)
obj2=Duder(3)
print(obj * obj2)
