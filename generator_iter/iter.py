#example of iter 

#first create an iterable object
iterbale=[1,2,3,4,5,6]

#implict calling of iterable object
for i in iterbale:
    print(i,end='\t')
print('\n')

#calling a iter object explicitly
#creating a iter object
itob=iter(iterbale)
flag=True
while(flag):
    try:
      print(next(itob),end='\t')
    except Exception:
       flag=False

#generator funtion
#any funtion that return anything using yield keyword is considered as generator funtion
def fibo(n):
   a,b=0,1
   count=1
   while(count<n):
      yield a
      a,b=b,a+b
      count+=1

print()
for i in fibo(10):
   print(i,end='\t')
       
