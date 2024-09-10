#this program is an example for placeing fstring 
string='helo'
fstring=f"{string}"
print(fstring)

#list compremenstiaton
#square of the number 
print([i**2  for i in range(1,11)])

#creating a list of charaters from a string
string='manojkumar'
print([c for c in string])

#crating a list of length of words in a sentence
 
sentence='helo i am aswin sandeep i am coming from kerala'
print([ len(i) for i in sentence.split() ])
#printing common multiple of 3 and 5
print([i for i in range(1,101) if i%3==0 and i%5==0])