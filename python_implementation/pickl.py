import pickle  as pc

#getting data 

di={1:'aswin',2:'sandeep',3:'manoj'}

d2={3:'aswin',2:'sandeep',3:'manoj'}

db={}

db['first_data']=di
db['second_data']=d2

#pickling seriazlizarion

b=pc.dumps(db)
print(b)

b=pc.loads(b)
print(b)