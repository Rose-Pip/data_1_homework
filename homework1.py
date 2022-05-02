#!/usr/bin/env python
# coding: utf-8

# # Google 

# In[19]:


import time
import datetime
import pandas as pd

ticker = 'GOOG'
period1 = int(time.mktime(datetime.datetime(2020, 1, 1, 0, 0).timetuple()))
period2 = int(time.mktime(datetime.datetime(2021, 1, 1, 23, 59).timetuple()))
interval = '1d' # 1d, 1m

query_string = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'

df = pd.read_csv(query_string)
print(df)
df.to_csv('GOOGLE.csv')


# # close price for google versus time 

# In[20]:


import matplotlib.pyplot as plt
df_google = pd.read_csv(r'GOOGLE.csv')
df_google.head()


# In[21]:


import numpy as np
x=np.array(df_google['Close'])
y=np.array(df_google['Date'])


# In[25]:


plt.figure(figsize=(30,30))
plt.rc('axes',labelsize=20)
plt.xticks(rotation=90)
plt.ylabel('Close Price for google')
plt.plot_date(y,x,linestyle='dashed')


# # Microsoft  

# In[28]:


import time
import datetime
import pandas as pd

ticker = 'MSFT'
period1 = int(time.mktime(datetime.datetime(2020, 1, 1, 0, 0).timetuple()))
period2 = int(time.mktime(datetime.datetime(2021, 1, 1, 23, 59).timetuple()))
interval = '1d' # 1d, 1m

query_string = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'

df = pd.read_csv(query_string)
print(df)
df.to_csv('MSFT.csv')


# # close price for microsoft

# In[30]:


import matplotlib.pyplot as plt
df_msft = pd.read_csv(r'MSFT.csv')
df_msft.head()


# In[31]:


import numpy as np
x=np.array(df_msft['Close'])
y=np.array(df_msft['Date'])


# In[32]:


plt.figure(figsize=(30,30))
plt.rc('axes',labelsize=20)
plt.xticks(rotation=90)
plt.ylabel('Close Price for Microsoft')
plt.plot_date(y,x,linestyle='dashed')

