#dictionary filtering using dictonary comprehensiation
dict1={"NFLX":4950,"TREX":2400,"FIZZ":1800, "XPO":1700}
squared_dict = {key: value  for key, value in dict1.items() if(value<2000)}
print(squared_dict)  


