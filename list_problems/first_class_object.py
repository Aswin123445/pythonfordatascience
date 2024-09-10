def square(x):
    return x*2
def cube(x):
    return x*2*2

list1=[square,cube]

for li in list1:
    print(li(4))