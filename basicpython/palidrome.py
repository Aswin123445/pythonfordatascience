data=input("enter the string you want to check")
isPalidrome=True
for i in range(len(data)):
    if(data[i]!=data[(-1-i)]):
       isPalidrome=False
       break
    else:
        isPalidrome=True
if isPalidrome:
    print("String is palidrome")
else:
    print("string is not palidrome")
       