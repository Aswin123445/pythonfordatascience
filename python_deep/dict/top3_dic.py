#Write a Python program to get the top three items in a shop. 
ni={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
#sorting in desending order
n=dict(sorted(ni.items(),key=lambda m:m[1],reverse=True))

#write a program to print a dictionary line by line
for k in ni:
    print(f"{k}:{ni[k]}")


#Write a Python program to count the number of items in a dictionary value that is a list. 
dili={'class':[10,20,30,40,50],'class2':[100,200,300,400,500]}
#find the cound of value
for x in range(len(dili)):
   print(len(list(dili.values())[x]))





    