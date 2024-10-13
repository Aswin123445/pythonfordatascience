import copy

a=[10]

b=copy.deepcopy(a)
print(id(a))
print(id(b))

#example for shallow copy

sh=[10]
s=copy.copy(sh)
print(s)
s.append(20)
print(s)
print(sh)