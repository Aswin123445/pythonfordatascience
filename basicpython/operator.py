import random
vowels='aswin sandeep and co'
vo=set([x for x in vowels  if x in ('a','e','i','o','u') ])
print(vo)
#creating random numbers from for a list of size 10

size=int(input("enter the size of the list: "))
ranlist=[]
for x in range(size) :
   ranlist.append(random.randint(1,500))

newlis=["fixx" if x%3==0 else "buzz" if x%5==0 else x for x in ranlist]
print(newlis)

lu=[x.upper() for x in vowels]
print(lu)

lc=[len(x) for x in vowels.split() ]
print(lc)

#creating a list of reversed word from the sentance
rl=[x[::-1] for x in vowels.split()]
print(rl)

#list of word that starts with vowels

lw=[ x  for x in vowels.split() if x[0] in ('a','e','i','o','u')]
print(lw)
lcw=[x for x in vowels.split() if len(x)>5]
print(lcw)

#dictionary comprehensiation
print({x:x**2 for x in range(1,11)})

dlist=[10,23,40,53,2,5,3]
print({x:x**2 for x in dlist if x%2==0})

words = ["apple", "banana", "cherry", "date"]

print({x:len(x) for x in words})

print({x:'even' if x%2==0 else 'odd' for x in range(1,11)   })

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

print({x:y for x,y in zip(keys,values)})

#merging two dictionary and adding the sum of the dictionay
di1={'a':10,'b':20,'c':30}
di2={'c':100,'b':200,'d':300}
print(set(di2)|set(di1))
for x in di1.keys():
   if x in di2.keys():
      di1[x]+=di2.pop(x)
print(di1|di2)
merged_dict={x:di1.get(x,0)+di2.get(x,0) for x in set(di1)|set(di2)}
print(merged_dict)

#using odd value delelet
ddddd={10:200,21:200,43:401}

dddd={x:y for x,y in ddddd.items() if y%2==0 }

for x,y in tuple(ddddd.items()):
   if x%2==0:
      del ddddd[x]
print(ddddd)

#print(dddd)

#factorial of the number
def fact(number):
   if number==0:
      return 1
   return number*fact(number-1)

print(fact(5))

#normao way
number=10
ans=1
while(number!=0):
   ans*=number
   number-=1
print(ans)