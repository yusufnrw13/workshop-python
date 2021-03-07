#!/usr/bin/env python
# coding: utf-8

# In[2]:


s = 'Hello, world.'
str(s)


# In[3]:


repr(s)


# In[4]:


str(1/7)


# In[5]:


x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)


# In[6]:


hello = 'hello, world\n'
hellos = repr(hello)
print(hellos)


# In[7]:


repr((x, y, ('spam', 'eggs')))


# In[8]:


import math
print(f'The value of pi is approximately {math.pi:.3f}.')


# In[9]:


print('We are the {} who say "{}!"'.format('knights', 'Ni'))


# In[10]:


for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # Note use of 'end' on previous line
    print(repr(x*x*x).rjust(4))


# In[11]:


import math
print('The value of pi is approximately %5.3f.' % math.pi)


# In[12]:


f = open('workfile', 'w')


# In[15]:


f = open('workfile', 'rb+')
f.write(b'0123456789abcdef')


# In[16]:


import json
json.dumps([1, 'simple', 'list'])


# In[ ]:




