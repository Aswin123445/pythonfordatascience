#operator overloading
class Operator:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    #operator overloading funtion
    def overloading1(self , a=0, b=0, c=0):
        if a==0 and b==0:
            return c
        elif a==0:
            return c+b 
        elif b==0:
            return a+c
        else:
            return a+b+c

Op=Operator(100,200,300)
print(Op.overloading1(10,20,30))
print(Op.overloading1(10))
print(Op.overloading1(40,50))