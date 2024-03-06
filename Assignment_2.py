#!/usr/bin/env python
# coding: utf-8

# In[3]:


def newstring(s):
    result = []

    for i in range(len(s)):
        current_char = s[i]
        ascii_value = ord(current_char)

        if ascii_value % 2 == 0:
            next_char = chr((ascii_value + (ascii_value % 7)) % 128)
            result.append(next_char)
        else:
            prev_char = chr((ascii_value - (ascii_value % 5)) % 128)
            result.append(prev_char)

    return ''.join(result)

# Example usage:
s = "abcde"
modified_string = newstring(s)
print("Original String:", s)
print("Modified String:", modified_string)


# In[ ]:




