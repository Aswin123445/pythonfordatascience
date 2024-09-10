#zero exception error 
number1=20
number2=0
#we will write the program that have the chances of getting error inside the try blcok
try:
    print("dividing two numbers")
    result=number1/number2
    print(result)
except ZeroDivisionError as e:
   print("something bad happend")
   print(e)