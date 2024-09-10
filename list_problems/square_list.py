list=[1,2,3,4,5,6]
#finding the square using list compremenstion

print([x**2 for x in list])

#make a list based on the even or odd number
#if the number is even then find the sqaure
#els find the cube of the number
print([x**2 if x%2==0 else x**3 for x in list])