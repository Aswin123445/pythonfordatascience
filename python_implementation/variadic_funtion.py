def varidadic_funtion(*value )->int:
    return sum(value)
print(varidadic_funtion(10,20,30,40))


def d():
    yield 1
    yield 2
    yield 3

#doing some simple decorator example
def decorator(fu):
    #wrapper funtion
    def wrapper():
        print('wrapper funtion is called')
        fu()
    return wrapper()
def fu():
    print("hellow world")

#calling decorator funtion 


    