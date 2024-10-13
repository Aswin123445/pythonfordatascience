print("this funtion will explains the importance of annotaion in python")
#decorator
def decorator(fun):
    #outter wrapper funtion
    def wrapper():
        #extra statements executed by the wrapper funtion
        print("hellow world the wrapper funtion is called")
        #calling the inner funtion
        fun()
        #returning the wrapper funtion
    return wrapper

#calling the funtion
def fun():
    print("inner funion is called")

decor=decorator(fun)
decor()


#type annotation
a=int(input("enter the number you want ot find the factorial: "))

#funtion to find the factorial
def fact(a: int)->bool:
    if a==1 :
        return 1
    else :
        return a * fact(a-1)


