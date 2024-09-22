#Write a Python program to find the key of the maximum
#  value in a dictionary. 

di={'Theodore': 329, 'Roxanne': 240, 'Mathew': 21, 'Betty': 20}
maxva=max(di.values())
for  d in di:
    if di[d]==maxva:
        print(d)
        break

max_key = max(di, key=di.get)
print(max_key)

di=dict(sorted(di.items(),key=lambda x:x[1]))
print(di)