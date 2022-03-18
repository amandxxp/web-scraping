#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import pandas as pd
import html2text


# In[2]:


headers = {
    'Host': 'api-publication-search-prd.azurewebsites.net',
    'Connection':'keep-alive',
    'Content-Length':'486',
    'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
    'Accept':'application/json',
    'Content-Type':'application/json',
    'sec-ch-ua-mobile':'?0',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36',
    'sec-ch-ua-platform': "Windows",
    'Origin':'https://www.brunel.net',
    'Sec-Fetch-Site':'cross-site',
    'Sec-Fetch-Mode':'cors',
    'Sec-Fetch-Dest':'empty',
    'Referer':'https://www.brunel.net/',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'en-US,en;q=0.9',
}
 


# In[3]:


title_s=[]
countryName_s=[]
city_s=[]
addressLine_s=[]
description_s=[]
totalYearsOfExperience_s=[]


# In[4]:


for j in range(1,6):
    json_data={"pageSize":12,
               "sortOrder":2,
               "page":1,
               "searchText":"engineering-it",
               "locationFilter":{
                   "location":"",
                   "range":0
               },"language":"en",
               "countryPreset":[
                   "AFG",
                   "ALA",
                   "ALB",
                   "ASM",
                   "AND",
                   "AGO",
                   "AIA",
                   "ATA",
                   "ATG",
                   "ARG",
                   "ARM",
                   "ABW",
                   "AUS",
                   "AZE",
                   "BHS",
                   "BHR",
                   "BGD",
                   "BLR",
                   "BLZ",
                   "BEN",
                   "BMU",
                   "BES",
                   "BIH",
                   "BGR",
                   "BFA",
                   "BDI",
                   "CAN",
                   "CHN",
                   "COG",
                   "COD",
                   "FRA",
                   "ATF",
                   "IND",
                   "IDN",
                   "JPN",
                   "KWT",
                   "MYS",
                   "MCO",
                   "NZL",
                   "POL",
                   "QAT",
                   "RUS",
                   "BLM",
                   "SAU",
                   "SGP",
                   "KOR",
                   "THA",
                   "ARE",
                   "GBR",
                   "USA",
                   "BEL",
                   "AUT",
                   "CZE"
               ],
               "currentLanguage":"en",
              }


# In[5]:


response = requests.post('https://api-publication-search-prd.azurewebsites.net/api/PublicationsSearch/Get', headers=headers, json=json_data)
data = response.json()


# In[6]:


data=data["publications"]
for i in range(0,len(data)):
        
    title=data[i]['title']
    if len(title) == 0:
        title_s.append("Not Found")
    else:
        title_s.append(title)
            
    countryName=data[i]['countryName']
    if len(countryName) == 0:
        countryName_s.append("Not Found")
    else:
        countryName_s.append(countryName)
            
    city=data[i]['city']
    if len(city) == 0:
        city_s.append("Not Found")
    else:
        city_s.append(city)
            
    addressLine=data[i]['addressLine']
    if len(addressLine) == 0:
        addressLine_s.append("Not Found")
    else:
        addressLine_s.append(addressLine)
            
    description=data[i]['description']
    description = html2text.html2text(description)
    if len(description) == 0:
        description_s.append("Not Found")
    else:
        description_s.append(description)
            
    totalYearsOfExperience=data[i]['totalYearsOfExperience']
    totalYearsOfExperience=str(totalYearsOfExperience)
    if len(totalYearsOfExperience) == 0:
        totalYearsOfExperience_s.append("Not Found")
    else:
        totalYearsOfExperience_s.append(totalYearsOfExperience)
            


# In[7]:


rdf = pd.DataFrame({"title" : title_s[:], "countryName" : countryName_s[:],"city":city_s[:],"addressLine":addressLine_s[:],"description":description_s[:],"totalYearsOfExperience":totalYearsOfExperience_s[:]})

rdf.to_csv('D:/brunelwebscrap.csv',index=False)


# In[ ]:




