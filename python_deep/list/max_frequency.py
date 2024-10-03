li=[ 3, 8, 4, 7, 9, 8, 6, 5, 1, 6, 1, 2, 3, 2, 4, 6, 9, 1, ]

#using dict comprehensiation
di={x: li.count(x) for x in li}
print(max(di.items(),key=lambda x:x[1])[0])

li=['aswin','sandeep']
print([i[0] for i in li])


