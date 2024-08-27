#creating a class with inputing two numbers
class Operation():
    def printhel(self):
        print('This page look for the operation')
class Result(Operation):
    def printhel(self):
        print('this page again look for the operation')
class Hi(Operation):
    def printhel(self):
        print('this page say helo')

o= Operation()
o.printhel()
o=Result()
o.printhel()
o=Hi()
o.printhel()

