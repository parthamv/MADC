#!/usr/bin/env python
# coding: utf-8

# In[14]:


import ipynb_checkpoints
from TopCrypto import topcrypto
from Crypto_History import CryptoHistory
from CryptoCurrent import Cryptocurrent
from CryptoPredict import CryptoPredict
from datetime import datetime
from Crypto_News import Crypto_News
import time, requests, pandas, lxml
from lxml import html
from dateutil.relativedelta import relativedelta
from datetime import datetime
import requests, pandas

# In[5]:


o = topcrypto() 
o.topcoins(10)


# In[6]:


my_string = str(input('Enter start date(yyyy-mm-dd hh:mm): ')) #2022-04-14 18:22
dt_start = datetime.strptime(my_string, "%Y-%m-%d %H:%M")
my_string1 = str(input('Enter end date(yyyy-mm-dd hh:mm): ')) #2022-04-15 18:22
dt_end=datetime.strptime(my_string1, "%Y-%m-%d %H:%M")
start=CryptoHistory.format_date(dt_start)
end=CryptoHistory.format_date(dt_end)
symbol = input("Enter the cryptocurrency symbol (i.e,'CRYPTO_NAME'-USD): ") #BTC-USD
r=CryptoHistory.subdomain(symbol, start, end)
head=CryptoHistory.header_function(r)
base_url = 'https://finance.yahoo.com'
url = base_url + r
data=CryptoHistory.scrape_page(url,head)
data[0].to_csv('Requested_CryptoPr.csv') ##Convert the dataframe to CSV file and store in path.
    


# In[7]:


def CryptoDate():
       
       """
   	Claculates the current time in the system as the end date and the 
       time 60 seconds prior to this as the end date and returns the same.
       
   	"""
       end_date = datetime.today()
       st_date = end_date - relativedelta(seconds = 60)
       return st_date,end_date


# In[8]:


st_date,end_date=CryptoDate()
Cryptocurrent.CryptoMain(st_date,end_date)


# In[15]:


crypto=CryptoPredict()
pred=crypto.pricePredict("SOL-USD","30-04-2022")


# In[10]:


crypto.visualizePredict(pred)


# In[11]:


cryptonews=Crypto_News()
cryptonews.crypto_news("BTC")


# In[12]:


cryptonews.crypto_news_df("BTC")


# In[ ]:




