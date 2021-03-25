#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup

url = "https://www.ligue1.fr/fr-FR/classement/buteurs"
#j=input('Quelle journee ? (0 pour derniere journee) : ')
#if j:url = "https://www.lfp.fr/ligue1/classement?journee1=0&journee2="+str(j)+"&cat=Gen"

result = requests.get(url, verify=False)
src = result.content


# In[183]:


soup = BeautifulSoup(src, 'lxml')
print(soup.prettify())


# In[6]:


table = soup.find(class_='player-stats-table')
print(table.prettify())


# In[7]:


head = table.find(class_='player-stats-table-heading')
print(head.prettify())


# In[25]:


table_head = head.find_all('div')
for s in table_head:
    print(s.contents[0], end='\t')


# In[26]:


print(table_head)


# In[27]:


body = table.find(class_='player-my-stats-table-body')
print(body.prettify())


# In[34]:


li_tags = body.find_all(class_='desktop-item')
#print(li_tags)
print(len(li_tags), li_tags[0].prettify())


# In[45]:


col = li_tags[0].find_all('div')
print(col[1].contents[2])
print(col[2].contents[2])
print(col[3].contents[2])
print(col[4].contents[0])


# In[65]:


row = {}
row[table_head[0].contents[0]] = col[0].contents[0]
row[table_head[1].contents[0]] = col[1].contents[2]
row[table_head[2].contents[0]] = col[2].contents[2]
row[table_head[3].contents[0]] = col[3].contents[2]
row[table_head[4].contents[0]] = col[4].contents[0]
print(row)


# In[72]:


def create_row(position):
    row = {}
    col =  li_tags[position].find_all('div')
    row[table_head[0].contents[0]] = col[0].contents[0]
    row[table_head[1].contents[0]] = col[1].contents[2].replace('\r\n','').strip()
    row[table_head[2].contents[0]] = col[2].contents[2].replace('\r\n','').strip()
    row[table_head[3].contents[0]] = col[3].contents[2].replace('\r\n','').strip()
    row[table_head[4].contents[0]] = col[4].contents[0].replace('\r\n','').strip()
    print(row)
    return row
rows = []    
for n in range(50):
    rows.append(create_row(n))


# In[73]:


import pandas as pd

df  = pd.DataFrame.from_dict(rows)
df


# In[74]:


df.info()


# In[75]:


df.iloc[:,4]=df.iloc[:,4].astype('int') 
#type(df.iloc[0,1])
df.info()


# In[76]:


df.set_index('POSITION', drop=True, inplace=True)
print(df)


# In[77]:


df.to_csv('ligue1_2020_buteurs.txt', sep = ',')


# In[78]:


# In[79]:


df.describe()


# In[80]:


def moyVar(X):
    n = len(X)
    if n==0:
        return None
    else:
        s1, s2 = 0, 0
        for x in X:
            s1 = s1 + x
            s2 = s2 + x*x
        m = s1/n
        return m,s2/n - m**2

def moyVarP(X, N):
    p1, p2 = len(X), len(N)
    if p1==0 or p2 != p1:
        return None
    else:
        s1, s2, n = 0, 0, 0
        for k in range(1,p1):
            n = n + N[k]
            z = N[k]*X[k]
            s1 = s1 + z
            s2 = s2 + z*X[k]
        m = s1/n
        return m,s2/n - m**2


# In[82]:


moyenne,variance=moyVar(df.Buts)

print('Supérieur à la moyenne', df[df.Buts>moyenne])


# In[84]:


import numpy as np
import matplotlib.pyplot as plt
l = len(df)
x = np.arange(l)
y = df.Buts
plt.plot(x,y)
plt.plot(x,np.ones(l)*moyenne)
plt.plot(x,np.ones(l)*variance)
plt.show()


# In[ ]:




