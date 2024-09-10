#checking the value exist in a dictionary or not
value1='sandeep'
value2='sandeep'
dict1={1:'aswin',2:'ramesh',3:'madhu'}

#getting the values
va=dict1.values()
#is it exist in dict
if value1 in va:
    print(f"{value1} exist in the list")
else :
    print(f"{value1} does not exist in the list")
