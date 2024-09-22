# Write a Python program to create a dictionary from a string.
# with values as frequecy
string=input("enter the string you want to make to dictionary \n: ")
dic={x:string.count(x) for x in string} 
print(dic)



#Write a Python program to sort a list alphabetically in a dictionary. 
di={1:
      ['aswin','sandeep','manojkumar','rajest'],
    2:
      ['radhika','rani','marilin','mnjil']
    }
#sorting
for k in di:
    di[k].sort()
print(di)