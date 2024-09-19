class Prime:
    """class to find the prime number"""
    def __init__(self,limit):
        self.__limit=limit

    @property
    def getter(self):
        return self.__limit
    
    @getter.setter
    def getter(self,value):
        self.__limit=value
    
    def primer(self):
        if self.__limit<2:
            return "not  a prime number"
        else:
            count=2
            while count**2<self.__limit:
                if self.__limit%count!=0:
                    count+=1
                else :
                    return "not a prime number"
            return "it's a prime number"
            
prime=Prime(15)
print(prime.primer())
                   

            




