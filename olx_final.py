#!/usr/bin/env python
# coding: utf-8

# In[9]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[10]:


url= 'https://www.olx.pl/d/dom-ogrod/meble/lozka/warszawa/q-ikea/'
page= 1
bed= []
while True: 
    response= requests.get(url)
    data= response.text
    soup= BeautifulSoup(data, 'html.parser')
    listing = soup.find_all('div', {'data-cy': 'l-card'})
    end_page= 'https://www.olx.pl' + soup.find_all('a', {'class': 'css-1mi714g'})[-1].get('href')
    for item in listing:
        name= item.find('h6', {'class': 'css-16v5mdi er34gjf0'}).text
        price_a= item.find('p', {'class':'css-10b0gli er34gjf0'}).text
        try:
            price_b= (list(int(p) for p in price_a if p.isdigit()==True))
            s=[str(i) for i in price_b]
            price= int(''.join(s))
        except Exception as e:
            price= None
        bed.append([name, price])

    page+=1 
    url= 'https://www.olx.pl/d/dom-ogrod/meble/lozka/warszawa/q-ikea/?page='+ str(page)
    if end_page==url:   
        break

olx_df= pd.DataFrame(bed, columns= ['name', 'price'] )


# In[11]:


print(olx_df['price'].mean())


# In[12]:


print(olx_df)


# In[ ]:




