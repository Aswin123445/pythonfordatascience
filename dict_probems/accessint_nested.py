ndict={'aswin':1,'a':2,'manoj':{'age':10,'place':'kerala'}}
#accessin the nested list
print(ndict['manoj']['age'])

#initiaialize a dict with default vaue with the set of values
tuple1=(1,2,4,5)
dict=dict.fromkeys(tuple1,'id')
print(dict)

#extracting keys from a dict
print(dict.keys())