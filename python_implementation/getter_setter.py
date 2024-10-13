#so i am going to type about what i know about 
class GetSet:
    def __init__(self , a)  :
        self.a=a
    @property
    def getter_a(self) :
        return self.a
    @getter_a.setter
    def setter_a(self, a):
        self.a=a
        
getset=GetSet(10)
print(getset.getter_a)