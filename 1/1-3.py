#!/usr/bin/env python
# coding: utf-8

# In[20]:


b = int(input())
if b == 0:
    print('ゼロ')
elif b == 1:
    print('いち')
elif b == 2:
    print('に')
else:
    print('たくさん')


# In[21]:


if a and b:
    print('OK')


# In[22]:


a = 3
if a == 3: print('OK')


# In[24]:


a, b, c = 7, 5, 3
if a > b > c:
    print('OK')


# In[26]:


a,b = 1,2
a and b


# In[28]:


a = 1
while a < 10:
    print(a, end=' ')
    a += 1
    if a == 5:
        break
else:
    print('END')


# In[31]:


for i in range(3):
    print(i, 'Hello')


# In[32]:


list(range(1, 10, 2))


# In[34]:


for i in range(1, 100):
    if i % 2 == 1:
        print(i, end=' ')
        continue
    if i % 5 == 0:
        break


# In[36]:


squares = []
for n in range(1, 6):
    squares.append(n**2)
squares


# In[39]:


squares = [n**2 for n in range(1,6)]
squares


# In[41]:


squares = [n**2 for n in range(1,6) if n % 2 == 1]
squares


# In[44]:


for i in range(10, 5, -1):
    print (i, end=' ' )


# In[45]:


hello = [n for n in 'Hello' if n in 'hello']
print(hello)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




