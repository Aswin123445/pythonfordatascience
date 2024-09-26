li={"a":[1,2,3],"b":1,"c":5,"d":[10,20]}

total_sum=0

for i in li.values():
    #finding sum
    if isinstance(i,list):
        total_sum+=sum(i)
    else:
        total_sum+=i
print(total_sum)
        
       
    
   
    
