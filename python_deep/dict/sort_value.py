#sort the value insdie the dictionary by asending and deesding order
un_dictionary={'aswin':22,'nickil':30,'ashwandh':26,'shuhaib':19}
# un_dictionary = dict(sorted(un_dictionary.items(), key=lambda item: item[1]))
# print("Ascending Order:", un_dictionary)

m=dict(sorted(un_dictionary.items(),key=lambda item:item[1]))
print(m)

#desending order
z=dict(sorted(un_dictionary.items(),key=lambda m :m[1],reverse=True))
print(z)


#sort value of dict by key value
key_dictionary={22:'aswin',30:'nickil',26:'ashwandh',19:'shuhaib'}
z=dict(sorted(key_dictionary.items(),key=lambda m :m[0],reverse=False))
print(z)



