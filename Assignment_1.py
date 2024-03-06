#!/usr/bin/env python
# coding: utf-8

# In[5]:


def substrings(s, x):
    result = []

    for i in range(len(s)):
        for j in range(i + x - 1, len(s)):
            if s[i] == s[j]:
                substring = s[i:j + 1]
                if len(substring) >= x:
                    result.append(substring)

    if result:
        min_length = len(min(result, key=len))
        result = [substring for substring in result if len(substring) == min_length]

        for substring in result:
            print(substring)
    else:
        print("not-found")

        
s = "abccdbacca"

x = 3
print("x =", x)
substrings(s, x)

x = 4
print("\nx =", x)
substrings(s, x)

x = 5
print("\nx =", x)
substrings(s, x)

x = 6
print("\nx =", x)
substrings(s, x)

x = 7
print("\nx =", x)
substrings(s, x)

x = 8
print("\nx =", x)
substrings(s, x)


# In[ ]:




