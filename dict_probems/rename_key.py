#rename key in the dictionary
dict1={1:'aswin',2:'sandeep',3:'madhu'}
#changing the key 
#empty dict

#changing the value
value1=5
dict2={}
for key,value in dict1.items():
    if key==2:
        dict2[value1]=value
    else :
        dict2[key]=value

print(dict2)
    