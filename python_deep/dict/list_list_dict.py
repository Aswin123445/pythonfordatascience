p={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
lis=[1,2,3,5]
print([[x]+[y] for x,y in p.items()])

#Write a Python program to filter even numbers from a dictionary of values. 
di={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
di={x:[i for i in y if i%2==0]for x,y in di.items()}
print(di)

#python program to convert the given list to a dictionary

tem=[[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]

t={x[0]:x[1:] for x in tem}
print(t)
