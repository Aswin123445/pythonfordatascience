ni={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}

#finding the sum
s=sum(ni.values())
#replacing existing value wiht sum

ni={x:s for x in ni}
print(ni)