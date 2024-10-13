#funtions inside funcitons
def outer(inner):
    inner()
def inner():
    print('inner funtion is called')
outer(inner)


#decorator  funtction 
def dec(inner):
    #wrapper funtion
    def wrapper():
        print("decoration funtion is called")
        inner()
    return wrapper
def inner():
    print("inner funtion is called")
decorated_funtion=dec(inner)
decorated_funtion()