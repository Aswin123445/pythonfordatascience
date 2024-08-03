#!/usr/bin/env python
# coding: utf-8

# In[3]:


#if statement is used to do particlular set of code based on the condition
x=int(input("Enter a number"))
if x<0:
  x=0
  print("x is a negative number")
elif x>0:
  print("entered number is positve number")
else:
  print("not")


# In[6]:


#for loop
words=["aswin","sandeep","manoj","sacariya"]
for w in words:
  print(w," ",len(w))


# In[8]:


#making a copy of the list and playing with the copy
for w in words[:]:
    print(w,len(w))
print(words)


# In[9]:


#the range funtion
for i in range(10):
    print(i)


# In[10]:


#range starting from another number
for i in range(1,10):
    print(i)


# In[13]:


#so inside for loop we can compine the len funtion and range funtion to make iteration
for w in range(len(words)):
    print (words[w])


# In[ ]:


# the pass sttement does nothing
while True:
    pass


# In[ ]:




