with open('pi.txt',newline='\n') as file_pi:
    read=file_pi.read()
print(read)

#reading line by line
with open('pi.txt',newline='\n') as file_pi:
    for line in file_pi:
      print(line.rstrip())

#converting the lines to list
line_list=[]
with open('pi.txt',newline='\n') as file_pi:
    for line in file_pi:
      line_list.append(line)
print(line_list)
#reading the line line by line

#writing to the file
with open('pi.txt','w') as file:
   statement='hi all i am aswin'
   file.write(statement)
with open('pi.txt') as file:
   print(file.read())

#appending to an existing file
with open('pi.txt','a') as file:
   statement='hi all i am aswin'
   file.write(statement)
with open('pi.txt') as file:
   print(file.read())

