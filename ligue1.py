# YouTube Link:

# Let's obtain the links from the following website:
# https://www.lfp.fr/ligue1/classement?cat=Gen

# One of the things this website consists of is records of presidential
# briefings and statements.

# Goal: Extract all of the links on the page that point to the
# briefings and statements.

debug = False
import requests
#To disable using Python code (requests < 2.16.0):
#from requests.packages.urllib3.exceptions import InsecureRequestWarning
#requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

#To disable using Python code (requests >= 2.16.0)
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup

url = "https://www.lfp.fr/ligue1/classement?cat=Gen"
j=input('Quelle journee ? (0 pour derniere journee) : ')
if j:url = "https://www.lfp.fr/ligue1/classement?journee1=0&journee2="+str(j)+"&cat=Gen"

result = requests.get(url, verify=False)
src = result.content
soup = BeautifulSoup(src, 'lxml')
div = soup.find_all('div')
if debug : print('div',div)
urls = []

id_tag = soup.find(id='classement_l1')
thead_tag = id_tag.find_all('thead')
tr_tag = id_tag.find_all('tr')
j_tag = soup.find(id='journee2')

def hasSelected(tag):
    if tag.name != 'option':
        return False
    try:
        if tag['selected']: return True
    except:
        return False
#search texte journee j
select_tag = soup.find_all('select')
#if debug : print('select_tag',select_tag[0].contents)
for child in select_tag[0].children:
    if hasSelected(child):
        saison=child.text
        break

for child in select_tag[2].children:
    if hasSelected(child):
        journee=child.text
        break

import collections
teams=[]
Team = collections.namedtuple("Team", ['Position', 'Club', 'Pts', 'J', 'G', 'N', 'P', 'Bp', 'Bc', 'Diff'], rename=False)

print('Classement',saison,journee)

data=[]
for t in thead_tag:
    d=()
    child=t.findChildren('th')
    for c in child:
        d+=(c.text,)
        if debug : print(c.text,end='\t')

data.append(d)
if debug : print()
if debug : print('data_head',data,'end')

pos=0

for a in tr_tag[1:]:
    pos+=1
    d=()
    child=a.findChildren('td')
    for c in child:
        if (c.string is None):
            d+=(c.findChild().text.strip(),)
            #if debug : print(c.findChild().text.strip(),end='\t')
        else:
            d+=(c.text,)
            #if debug : print(c.string,end='\t')
    if debug : print(d)

    data.append(d)
    teams.append(Team(*d))
'''
for k in data:
    if debug : print(k,len((k)))
    print('%8s\t%-25s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % k)
    #if debug : print('%s\t%s\t\t\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % ('Position', 'Club', 'Pts', 'J', 'G', 'N', 'P', 'Bp', 'Bc', 'Diff.'))
    #if debug : print("{}\t{}\t\t\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}{}".format(*k))
'''
def ratio(t,p):
    return int((int(p)/int(t.J))*100)/100

def statistics():
    print('%-25s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % ('Club','Pts','J','G','N','P','Bp','Bc','Diff','Pts/J','Bp/J','Bc/J'))
    for t in teams:
        print('%-25s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (t.Club,t.Pts,t.J,t.G,t.N,t.P,t.Bp,t.Bc,t.Diff,round((3*int(t.G)+int(t.N))/int(t.J),2),round(int(t.Bp)/int(t.J),2),round(int(t.Bc)/int(t.J),2)))

#statistics()

#print(data,len(data))
import pandas as pd
df = pd.DataFrame(data)
df.to_csv('data.txt', sep = ',')
#df.iloc[1,2]
print('a',df)

df.columns=df.iloc[0,:] #rename columns labels with row 0
df.to_csv('data2.txt', sep = ',')
print('b',df)

df.drop(0, axis=0, inplace=True) #drop row 0
df.to_csv('data3.txt', sep = ',')
print('c',df)

df.set_index('Position', drop=True, inplace=True)
df.to_csv('data4.txt', sep = ',')  #csv correct
print('d',df)

#convert columns str to int
for i in range(1,9):
    #print(df.iloc[:,i])
    df.iloc[:,i]=df.iloc[:,i].astype('int') 
#type(df.iloc[0,1])
print('e')
df.info()
#df.drop('Position', axis=1, inplace=True)  #drop column Position
#df.rename(columns=df.iloc[1])

# add column with computed values
df['Pts/J']=df.iloc[:,1]/df.iloc[:,2]
df['Bp/J']=df.iloc[:,6]/df.iloc[:,2]
df['Bc/J']=df.iloc[:,7]/df.iloc[:,2]
print('f',df)

print('g')
df.info()
df.to_csv('ligue1_csv')

df = pd.read_csv('ligue1_csv')

print('h',df.describe())

print('i',df.describe().loc['mean'])

print('j',df.describe().loc[['mean','std']])

print('k',df.describe().columns)
print('l')
df.info()


def moyVar(X):
    n = len(X)
    if n==0:
        return None
    else:
        s1, s2 = 0, 0
        for x in X:
            s1 = s1+x
            s2 = s2+x*x
        m = s1/n
        return m,s2/n - m**2

moyVar(df.Pts)    