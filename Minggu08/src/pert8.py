#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
os.getcwd() 


# In[2]:


os.chdir('/server/accesslogs')   # Change current working directory
os.system('mkdir today')


# In[4]:


import glob
glob.glob('*.py')


# In[5]:


import sys
print(sys.argv)


# In[6]:


sys.stderr.write('Warning, log file not found starting a new one\n')


# In[7]:


import re
re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')


# In[8]:


re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')


# In[9]:


import math
math.cos(math.pi / 4)


# In[10]:


math.log(1024, 2)


# In[ ]:


from urllib.request import urlopen
with urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl') as response:
    for line in response:
        line = line.decode('utf-8')  # Decoding the binary data to text.
        if 'EST' in line or 'EDT' in line:  # look for Eastern Time
            print(line)



import smtplib
server = smtplib.SMTP('localhost')
server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
"""To: jcaesar@example.org
From: soothsayer@example.org

Beware the Ides of March.
""")
server.quit()


# In[11]:


# dates are easily constructed and formatted
from datetime import date
now = date.today()
now


# In[12]:


now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")


# In[13]:


# dates support calendar arithmetic
birthday = date(1964, 7, 31)
age = now - birthday
age.days


# In[14]:


import zlib
s = b'witch which has which witches wrist watch'
len(s)


# In[15]:


t = zlib.compress(s)
len(t)


# In[16]:


zlib.decompress(t)


# In[17]:


zlib.crc32(s)


# In[18]:


from timeit import Timer
Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()


# In[19]:


Timer('a,b = b,a', 'a=1; b=2').timeit()


# In[ ]:




