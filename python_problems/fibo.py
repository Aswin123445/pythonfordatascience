def fibo(number):
    a,b=0,1
    while(a<number):
        print(a,end="\t")
        a,b=b,a+b
fibo(10)