#!/usr/bin/env python
# coding: utf-8

# ### Task 1:
#     

# In[1]:


# 1.Jupyter Install
print("hello world")


# In[21]:


# 2
a=[]
for i in range(2000,3201):
    if i % 7 == 0 and i % 5 != 0:
        print(i,end=',')  


# In[25]:


# 3
name=input("Enter your first name:")
lastname=input("Enter your last name:")
print(lastname +" "+ name)


# In[30]:


# 4
diameter = 12
volume=(4/3)*(3.14)*(diameter/2)**3
print("volume of sphere whose  diameter is {} = {}".format(diameter,volume))


# ### Task 2

# In[32]:


# 1
valueenter=input("Enter the comma-separated number")
a=valueenter.split(',')
print(a)


# In[54]:


# 2
for i in range(1,6,1):
    for j in range(1,i+1): 
        print('*',end='')
    print()
for i in range(4,0,-1):
    for j in range(i+1,1,-1):
        print('*',end='')
    print()


# In[55]:


# 3
text=input("enter your word ")
print(text[::-1])


# In[ ]:


# 4
"""
not able to slove this """

