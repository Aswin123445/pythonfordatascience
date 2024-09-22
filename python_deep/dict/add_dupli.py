#Write a Python program to combine two dictionary by adding values for common keys. 
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d1={x:d1.get(x,0)+d2.get(x,0) for x in  set(d1)|set(d2)}
print(d1)

#another way

#distic values in a dictionary

print(set(d1.values()))
