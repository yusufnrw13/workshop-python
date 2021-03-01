#!/usr/bin/env python
# coding: utf-8

# In[31]:


import fibonacci
def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result


# In[28]:


from fibonacci import *
fib(500)


# In[41]:


import sys
sys.ps1


# In[42]:


sys.ps2


# In[47]:


sys.ps1 = 'C> '
print('Yuck!')


# In[52]:


import fibonacci, sys
dir(fibo)


# In[53]:


dir(sys)


# In[54]:


import builtins
dir(builtins)


# In[ ]:




