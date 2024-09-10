#python funtion to sort the list
sort_list=[30,40,60,30,10]
#temporay sorting
print(list(sorted(sort_list,reverse=True)))
print(list(sorted(sort_list,reverse=False)))

#permenent sorting
sort_list.sort()
print(sort_list)
