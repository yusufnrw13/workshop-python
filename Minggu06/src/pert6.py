#!/usr/bin/env python
# coding: utf-8

# In[2]:


while True print('Hello world')


# In[ ]:





# In[3]:


10 * (1/0)


# In[4]:


4 + spam*3


# In[5]:


'2' + 2


# In[ ]:


while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")


# In[ ]:


raise NameError('HiThere')


# In[ ]:


class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class TransitionError(Error):
    """Raised when an operation attempts a state transition that's not
    allowed.

    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    """

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message


# In[ ]:


try:
    raise KeyboardInterrupt
finally:
    print('Goodbye, world!')

Goodbye, world!
KeyboardInterrupt


# In[ ]:




