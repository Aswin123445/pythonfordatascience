word="aswin Sandeep"
print(word.find('a',4,6))

class Checking:
    def __init__(self,value):
        self._value=value
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self,data):
        #performing some validation 
        if data>90:
          self._value=data

obj=Checking(10)
print(obj.value)
obj.value=91
print(obj.value)



