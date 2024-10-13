

file=open('helo.txt','w')
file.write('aswin sandeep')
file.close()
file=open('helo.txt','r')
text=file.readline()
print(text)
file.close()

with open ('helo.txt','r') as f:
    print(f.read())
