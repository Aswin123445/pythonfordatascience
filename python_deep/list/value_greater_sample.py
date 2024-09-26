#Write a Python program to find all the values in a list that 
# are greater than a specified number. 
lis=[10,20,5,3,49,4,66,54,65,7,3,12,17]
key=int(input("please enter the key you want to find: "))
print([x for x in lis if x >key])

# Write a Python program to remove 
# duplicates from a list of lists

li=[[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
ne=list(set([tuple(x) for x in li]))
ne=[list(n) for n in ne]
print(ne)