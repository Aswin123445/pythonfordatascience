#delete a dictonary based on the given conditon met

#if the key is even

di={'aswin':11,'sandeep':21,'radhir':30,'mardhi':40}

di={x:di[x] for x,y in list(di.items()) if y%2==0 }
print(di)

#using del keyword
for x,y in list(di.items()):
    if y%2==0:
        del di[x]
print(di)

