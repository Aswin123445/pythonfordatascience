#nested if statement inside the list compresiation allows us to apply multiply statemets 
# to the same value to the list
li=[10,20,40,3,5,14,54,53,22,30]
#list compresiation
#sorting number which is both multiple of 10 and 3
com=[x for x in li if x%3==0  if x%10==0 ]
print(com)

#adding 10 if the first condition is met else adding 20
ch = [x + 10 if x % 3 == 0 else x + 20  for x in li if x % 3 == 0 or x % 10 == 0]
print(ch)

#make a list if the x*2 if x is dividable by 20 or x*3 if x is is dividable by 7 or x is diviable by 11
ch=[x * 2 if x % 20 == 0 else x * 3 if x % 7 == 0 else x*4  for x in li if x%20==0 or x%7==0 or x%11==0]
print(ch)

#flattering a list of list using list compresiation
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print([num for row in matrix for num in row])

#list compresiation using fuctions
#create a funtion to find the factorial
def factorial_num(num):
    fact=1
    for i in range(1,num):
        fact*=i
    return fact
data_set=[3,4,5,6]
fact=[factorial_num(x) for x in data_set]
print(fact)

