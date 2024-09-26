li=[10,20,30,40,60]
gen=(x for x in li)
print(next(gen))
print(next(gen))
while True:
    try:
        ele = next(gen)
        print(ele)  # Now print the element
    except StopIteration:
        break
