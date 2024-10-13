lis=[10,20,33,43,22,53,54,20,12,33]
#fucitons to use the filter
def is_odd(data):
    if data%2 == 0 :
        return False
    else:
        return True
d=filter(is_odd,lis)
print(d)