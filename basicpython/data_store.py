#here we are going to store the data
import json

user_list=[]
flag=True
while flag:
    data=int(input("enter the age of the person"))
    user_list.append(data)
    key = input("is that the last user? y,n")
    flag = False  if key == 'y' else  True

#opening file to dump data
with open('new_list.json','w') as file:
    #writing the data
    json.dump(user_list, file)

#getting the stored data from the stored data

#opening file 
with open("new_list.json",'r') as file :
     #getting the json data to variable
     list=json.load(file)
print(list)



