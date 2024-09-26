# Write a Python function that takes two lists and returns True if they have at least one common member.
li1=[10,20,30]
li2=[40,50,60,70]
def is_common(li1,li2):
    for x in li1:
        if x in li2:
            return True
    return False
print(is_common(li1,li2))

# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. 
sli=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#deleting the specified position
ti=(0,4,5)
sli=[sli[x] for x in range(len(sli)) if x not in ti]
print(sli)