import csv
import json
import pickle
mapper=[]
with open('railway.csv','r') as reader:
    rea=csv.DictReader(reader)
    data=list(rea)
    print(len(data))
    for i in range(len(data)):
        mapper.append({'code':data[i]['CODE'],'name':data[i]['STATION NAME']})
    print(mapper)
    
