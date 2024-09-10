# count the occurance of same item in the list
list=[10,20,10,3,4,54,10,32,10,40]
#occurance count using compresiation
count=[i for i in list  ].count(10)
print(count)

#traditianal way 
num=int(input("enter the number you want to find the output"))
c=0
if num in list:
   for i in list:
      if i==num:
         c+=1
   print(f"the occurance of the number {num} is {c}")
else:
   print("no occurance of the number")
