# YouTube Link:

# Let's obtain the links from the following website:
# https://www.lfp.fr/ligue1/classement?cat=Gen

# One of the things this website consists of is records of presidential
# briefings and statements.

# Goal: Extract all of the links on the page that point to the
# briefings and statements.

debug = False
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from bs4 import BeautifulSoup

url = "https://www.lfp.fr/ligue1/classement?cat=Ext"
j=input('Quelle journee ? (0 pour derniere journee) : ')
if j:url = "https://www.lfp.fr/ligue1/classement?journee1=0&journee2="+str(j)+"&cat=Ext"

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

print('Classement Extérieur',saison,journee)

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
    print('%25s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % ('Club','Pts','J','G','N','P','Bp','Bc','Diff','Pts/J','Bp/J','Bc/J'))
    for t in teams:
        print('%25s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (t.Club,t.Pts,t.J,t.G,t.N,t.P,t.Bp,t.Bc,t.Diff,round((3*int(t.G)+int(t.N))/int(t.J),2),round(int(t.Bp)/int(t.J),2),round(int(t.Bc)/int(t.J),2)))

print()    
statistics()
