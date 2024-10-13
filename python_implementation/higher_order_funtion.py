lis=[10,21,30,40,50]

a=map(lambda x: x*5 ,lis)
print(next(a))

#filter 
print(list(filter(lambda  x: x*2 if x%2==0 else None,a)))

#reduce funtion 

