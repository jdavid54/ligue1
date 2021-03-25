#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Jean
#
# Created:     20/09/2019
# Copyright:   (c) Jean 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# YouTube Link:

# Let's obtain the links from the following website:
# https://www.lfp.fr/ligue1/classement?cat=Gen

# One of the things this website consists of is records of presidential
# briefings and statements.

# Goal: Extract all of the links on the page that point to the
# briefings and statements.

import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup

url = "https://www.lfp.fr/ligue1"
#j=input('Quelle journee ? (0 pour derniere journee) : ')
#if j:url = "https://www.lfp.fr/ligue1/classement?journee1=0&journee2="+str(j)+"&cat=Gen"

result = requests.get(url, verify=False)
src = result.content
soup = BeautifulSoup(src, 'lxml')


div = soup.find(id='tableaux_rencontres_ligue1')
#print(div.prettify())

def list_td(tr_tag):

    td_tags = tr_tag.find_all('td')
    if len(td_tags)<4: return
    #print(td_tags)
    print(td_tags[0].text,td_tags[1].text.strip(),'-',td_tags[5].text.strip(),'(',td_tags[6].text.strip(),')')

#table_tags = []
h4_tags = div.find_all('h4')
for h4_tag in h4_tags:
    print(h4_tag.text)
    #table_tags.append(h4_tag.next_sibling.next_sibling)
    table_tag=h4_tag.next_sibling.next_sibling
    tr_tags = table_tag.find_all('tr')
    #print('tr_tags',tr_tags,len(tr_tags))
    for tr in tr_tags[1:]:
        #print('tr',tr,type(tr))
        list_td(tr)
    print('===============================================')
