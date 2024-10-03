#Write a Python program to get the cumulative
#  sum of the elements of a given list.Sample Output
li=[1, 2, 3, 4]
def sumer(i,s):
     s[0]+=i
     return s[0]
s=[0]
print([sumer(i,s) for i in li])

#li = [1, 2, 3, 4]

def sumer(i, current_sum):
    return current_sum 

current_sum = 0
sums = [sumer(i, current_sum := current_sum + i) for i in li]
print(sums) 



