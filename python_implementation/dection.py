li = [ 'aswin' , 'sandeep' , 'manoj']
li1 = [1,2,3,]

print(dict(zip(li,li1)))

d='aswin sandeep'

print({i:d.count(i) for i in d  if i != ' '})

a = {'aswin':10 , 'sandeep':20 , 'manoj':2}

print(dict(sorted(a.items(),key=lambda i : i[1])))

# top three item in a shop

item = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
print(dict(sorted(item.items(),key=lambda x :x[1],reverse=True)[:3]))

d = {
    'a': [1, 2, 3],
    'b': [4, 5],
    'c': [6, 7, 8, 9]
}
print({i: sum(j) for i,j in d.items()})

