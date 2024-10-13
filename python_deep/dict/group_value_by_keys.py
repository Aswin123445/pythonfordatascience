dicts = [{'a': 1, 'b': 2}, {'a': 3, 'c': 4}, {'b': 5, 'c': 6}]

di={}

for i in range(len(dicts)):
    for x in dicts[i].keys():
        if x in di:
            di[x].append(dicts[i][x])
        else:
            di[x]=[dicts[i][x]]
print(di)
st=''
address='1.1.1.1'
for i in address:
    if i.isdigit():
        st+=i
    else:
        st+='[.]'
print(st)
h=''
