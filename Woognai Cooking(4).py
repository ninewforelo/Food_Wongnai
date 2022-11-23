#!/usr/bin/env python
# coding: utf-8

# In[29]:


import csv
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException


# In[30]:


options = Options()

options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'

driver = webdriver.Firefox(executable_path=r'C:\Users\COM01\Documents\Pliwlom\DSI 314\geckodriver.exe', options=options)

driver.get('https://www.wongnai.com')


# In[31]:


def get_url(search_term):
    template = 'https://www.wongnai.com/recipes?q=%E0%B8%A0%E0%B8%B2%E0%B8%84%E0%B9%83%E0%B8%95%E0%B9%89&sort.type=1'
    search_term = search_term.replace(' ' , '+')
    return template.format(search_term)


# In[32]:


url = get_url('รวม เมนูภาคใต้')
print(url)


# In[33]:


driver.get(url)


# In[34]:


soup = BeautifulSoup(driver.page_source,'html.parser')


# In[37]:


results = soup.find_all('div',{'class':'sc-5qrr3t-1 sc-5qrr3t-4 cAnJfo'})


# In[38]:


len(results)


# In[53]:


results[0].find('h2',{'class':'sc-5qrr3t-6 klzfDm'}).get_text()


# In[40]:


results[0].find('p',{'class':'sc-6u9vr3-0 fLZVAW sc-5qrr3t-9 jkgRbR'}).get_text()


# In[41]:


results[0].find('span',{'class':'hovx2z-3 ddVYsI ownerName'}).get_text()


# In[57]:


product_name = []
product_viewer = []
recipe_by = []

website = 'https://www.wongnai.com/recipes?q=%E0%B8%A0%E0%B8%B2%E0%B8%84%E0%B9%83%E0%B8%95%E0%B9%89&sort.type=1' 
driver.get(website)

while True:
    try:
        btn = driver.find_element_by_css_selector(".sc-AxiKw").click()
    except NoSuchElementException:
        break
            
    soup = BeautifulSoup(driver.page_source,'html.parser')
    results = soup.find_all('div',{'class':'sc-5qrr3t-1 sc-5qrr3t-4 cAnJfo'})
    for result in results:
        try:
            product_name.append(result.find('h2',{'class':'sc-5qrr3t-6 klzfDm'}).get_text())
        except:
            product_name.append('n/a')
        try:
            product_viewer.append(result.find('p',{'class':'sc-6u9vr3-0 fLZVAW sc-5qrr3t-9 jkgRbR'}).get_text())
        except:
            product_viewer.append('n/a')
        try:
            recipe_by.append(result.find('span',{'class':'hovx2z-3 ddVYsI ownerName'}).get_text())
        except:
            recipe_by.append('n/a')


# In[58]:


Woognai_Cooking = pd.DataFrame({'Name':product_name , 'Viewer':product_viewer,'Recipe by':recipe_by})


# In[59]:


Woognai_Cooking


# In[60]:


Woognai_Cooking.to_excel('Woognai_Cooking.xlsx',index=False)


# In[ ]:




