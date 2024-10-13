#ternary operator example
import random
a=random.randint(10,100)
print("helo world" if a<50 else "print this is complicated")

#nested list
print("helo world" if a<20 else "print this is 75 less" if a<75 else "prnt this number greater than 75" )
print(a)