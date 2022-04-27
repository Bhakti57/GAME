#!/usr/bin/env python
# coding: utf-8

# In[6]:


import random
computer_number=random.randrange(1,201)
user_number=int(input("Enter The Number: "))
print("Computer Number is ",computer_number)
if computer_number<user_number:
    print("You guess high number than computer number.")
elif computer_number>user_number:
    print("You guess low number than computer number.")
else:
    print("You guess equal number.")


# In[ ]:




