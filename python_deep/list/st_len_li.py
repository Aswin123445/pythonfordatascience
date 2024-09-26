#Write a Python program to count the number of strings 
# from a given list of strings. The string length is 2 or more and the first and last characters are the same. 

li=['abc', 'xyz', 'aba', '1221']
print(len([x for x in li if x[0]==x[-1] and len(x)>1]))