#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n=int(input())
f=input()
m=input()
count_r =m.count('r')
count_m =m.count('m')
list1 = [i for i in f]

for i in f:
    if i == 'r':
        if count_r== 0:
            print(len(list1), end = '')
            break
        count_r -=1
        list1.pop(0)
        
    elif i =='m':
        if count_m== 0:
            print(len(list1),end = '')
            break
        count_m -=1
        list1.pop(0)
    else:
        print(0, end = '')


# In[ ]:





# In[ ]:




