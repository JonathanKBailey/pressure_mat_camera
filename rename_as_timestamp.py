#!/usr/bin/env python
# coding: utf-8

# In[7]:


import os
import datetime
import shutil


# In[3]:


camera_path = os.path.join('data', 'camera_data')


# In[18]:


for root, dirs, files in os.walk(camera_path):
    if files:
        for f in files:
            if '1D' not in f:
                fp = os.path.join(root, f)
                tm = os.path.getmtime(fp)
                dtts = datetime.datetime.fromtimestamp(tm)
                ts = dtts.strftime('%Y-%m-%dT%H_%M_%S.%f%z')
                to_name = f'frame_{ts}.csv'
                tp = os.path.join(root, to_name)
                if not os.path.exists(tp):
                    shutil.copy(fp, tp)
                    shutil.copystat(fp, tp)
                    print(root, f, '->', tp)


# In[13]:


for root, dirs, files in os.walk(camera_path):
    if files:
        for f in files:
            if 'Cont' not in f:
                fp = os.path.join(root, f)
                os.remove(fp)


# In[ ]:




