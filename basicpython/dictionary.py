#create a dictionary
dict={'aswin':'bus','anoop':'bike','anup':'taxi'}
print(dict)

#accesing members through get method
print(dict.get('aswin',"value does not exitst"))

#output when the values is not exist
print(dict.get('athul','no value found'))

#looping through the dict
for key,value in dict.items():
    print(f"value of key is {key}\nvalue of value is {value}\n")

#looping through the key
for key in dict:
    print(key)

#looping through key usngin keys() method
for key in dict.keys():
    print(key)

#making a list of dictionary
person={'name':'aswin','age':21,'place':'kannur'}
list_person=[]
for i in range(30):
    list_person.append(person)
for list1 in list_person[25:]:
    print(list1)


