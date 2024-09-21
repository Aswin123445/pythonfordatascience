# Write a Python script to concatenate the following dictionaries to create a new one. 

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,1:60}

#containation using dict compresiation
dic4={**dic1,**dic2,**dic3}
print(dic4)

#adding the number if same key is found
dic4={x:dic1.get(x,0)+dic2.get(x,0)+dic3.get(x,0) for x in set(dic1)|set(dic2)|set(dic3)}
print(dic4)
