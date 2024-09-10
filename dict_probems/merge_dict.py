dict1={'aswin':11,'manoj':15,'raghesh':18}
dict2={'arun':24,'manoj':18,'aswin':22}
#as the name contianes the same key then the dict that
#pass as arguments will override the value
#using the update method
dict1.update(dict2)
print(dict1)

#using dict comprehsiation
dict11={'aswin':11,'manoj':15,'raghesh':18}
dict22={'arun':24,'manoj':18,'aswin':22}
print({**dict11,**dict22})
