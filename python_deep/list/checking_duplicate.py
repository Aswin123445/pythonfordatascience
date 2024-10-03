#Write a Python program to check if there are duplicate values in a given flat list. 
li=[1, 2, 3, 4, 5, 6, 7,6]
if True in [True for i in li if li.count(i)>1]:
    print ("value as this attribute")

#another way change the list to a set 
if len(li)==len(set(li)):
    print("list has no duplicate")

nums = [10, 20, 30, 40, 50, 60, 70]
nth = 6

result = nums[4::2]
print(result)
    

