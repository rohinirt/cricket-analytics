#!/usr/bin/env python
# coding: utf-8

# # Problem statement: IS MSD good enough to bat
# 

# In[2]:


import warnings
warnings.filterwarnings('ignore')
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

#to display all row column and columns
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
pd.set_option('display.expand_frame_repr',False)
pd.set_option('max_colwidth',-1)


# In[3]:


df = pd.read_csv('Desktop\cricket dataset\MAS-ACA-Masterclass-main\CSV Files\deliveries_updated_mens_ipl.csv')


# In[4]:


df.head()


# In[5]:


df['batsman_runs'].unique()


# In[6]:


df1 = pd.read_csv('Desktop\cricket dataset\MAS-ACA-Masterclass-main\CSV Files\matches_updated_mens_ipl.csv')


# df1.head()

# In[7]:


df1.head()


# In[ ]:





# In[8]:


df3 = pd.merge(df,df1,on = 'matchId',how= 'inner')


# In[9]:


df3.head()


# In[10]:


df3 = pd.merge(df,df1,on = 'matchId',how= 'inner')


# In[11]:


df4 = df3[df3['batsman'] == 'MS Dhoni']


# In[12]:


df4.head()


# In[13]:


df4['season'].unique()


# In[ ]:





# In[14]:


df4['season'].unique()


# In[ ]:





# In[15]:


df4.batsman_runs.sum()


# In[16]:


df4.batsman_runs.unique()


# In[17]:


len(df4)


# In[18]:


len(df4['ball'].unique())


# In[19]:


df4.groupby(['season',])['batsman_runs'].sum().head(15)


# In[20]:


run_by_season = pd.DataFrame(df4.groupby(['season',])['batsman_runs'].sum()).reset_index()


# In[21]:


ball= pd.DataFrame(df4.groupby(['season',])['ball'].count()).reset_index()


# In[22]:


ball.head()


# In[23]:


msdf = run_by_season.merge(ball, on = 'season', how = 'left')


# In[24]:


msdf.head()


# In[25]:


msdf['SR'] = msdf.apply(lambda x: 100*(x['batsman_runs']/x['ball']), axis = 1)


# 

# In[26]:


msdf.head()


# In[27]:


plt.figure(figsize = (16, 8))
plt.scatter(msdf.season,msdf.batsman_runs)
plt.xlabel('year')
plt.ylabel('runs')
for i in range(len(msdf)):
    plt.text(msdf['season'][i],msdf['batsman_runs'][i],msdf['SR'][i])

plt.show()


# In[28]:


plt.figure(figsize = (16, 8))
plt.scatter(msdf.season,msdf.SR)
plt.xlabel('year')
plt.ylabel('strike Rate')
for i in range(len(msdf)):
    plt.text(msdf['season'][i],msdf['SR'][i],msdf['batsman_runs'][i])

plt.show()


# In[29]:


plt.figure(figsize = (16, 8))
plt.scatter(msdf.batsman_runs,msdf.SR)
plt.xlabel('Runs')
plt.ylabel('strike Rate')
for i in range(len(msdf)):
    plt.text(msdf['batsman_runs'][i],msdf['SR'][i],msdf['season'][i])

plt.show()


# In[30]:


df4.head()


# In[31]:


ldf = df4[(df4.season >= 2019) & (df4.season <= 2022)]


# In[32]:


ldf.reset_index()


# In[33]:


df4['isSix'] = df4['batsman_runs'].apply(lambda x: 1 if x == 6 else 0)
df4['isFour'] = df4['batsman_runs'].apply(lambda x: 1 if x == 4 else 0)


# In[34]:


df4.head()


# In[35]:


six= pd.DataFrame(df4.groupby(['season',])['isSix'].sum()).reset_index()


# In[36]:


fours= pd.DataFrame(df4.groupby(['season',])['isFour'].sum()).reset_index()


# In[37]:


fours.head()


# In[38]:


six.head(16)


# In[39]:


df4= df4[(df4.over >= 15) & (df4.over <= 19)]


# In[49]:


plt.figure(figsize = (14, 8))
plt.bar(six.season,six.isSix)
plt.ylabel('No. of sixes')
plt.xlabel('Year')
plt.title('sixes in death over')


# In[41]:


msdf.head()


# In[42]:


msdf1 = six.merge(fours, on = 'season', how = 'left')


# In[43]:


msdf['isSix'] = df['batsman_runs'].apply(lambda x: 1 if x == 6 else 0)
msdf['isFour'] = df['batsman_runs'].apply(lambda x: 1 if x == 4 else 0)


# In[44]:


msdf['isDot'] = df['batsman_runs'].apply(lambda x: 1 if x == 0 else 0)


# In[45]:


msdf1.head()


# In[46]:


msdf1['boundries']=msdf1['isSix']+msdf1['isFour']


# In[47]:


msdf1.head()


# In[48]:


plt.figure(figsize = (16, 8))
plt.bar(msdf1.season,msdf1.boundries)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




