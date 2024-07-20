#!/usr/bin/env python
# coding: utf-8

# In[1]:


#getting comfortable with funtions used in list
list=[1,2,48,54,33,299,45,73]


# In[2]:


#adding element at the end
list.append(40)
print(list)


# In[3]:


#extend funtion can be used to add new list to the existing list and extend it
list2=[100,299,499]
list.extend(list2)


# In[4]:


print(list)


# In[6]:


#insert funtion can be used to insert the elments at any position
list.insert(5,40)
print(list)


# In[11]:


#remove funtion can be used to remove the first element that matches with the argument given to funtin
print(list)
list.remove(48)
print(list)


# In[12]:


#pop funtion can be used to remove the list from the given position
list.pop()


# In[13]:


print(list)


# In[14]:


#pop funtion delete if the postion is not give and output the deleted value to the terminal
list.pop(4)


# In[16]:


#count funtion is used to count number of times the number repeated
list.count(1)


# In[17]:


#sort funtion is used to sort all the elements in the list
list.sort()


# In[18]:


print(list)


# In[19]:


list.sort(reverse=True)


# In[20]:


print(list)


# In[21]:


#if the give the value of default argument of reverse at true the llist will be in reverse order


# In[22]:


#clear funtion is used to clear all the elements of the array
list.clear()


# In[23]:


print(list)


# In[ ]:




