#!/usr/bin/env python
# coding: utf-8

#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Jean
#
# Created:     20/09/2019
# Copyright:   (c) Jean 2019
# Licence:     Open source
#-------------------------------------------------------------------------------

# YouTube Link:

# Let's obtain the links from the following website:
# https://www.ligue1.fr/

# One of the things this website consists of is records of presidential
# briefings and statements.

# Goal: Extract all of the links on the page that point to the
# briefings and statements.

import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup

debug = False
save = False

url = "https://www.ligue1.fr/calendrier-resultats?seasonId=2019-2020&matchDay=26"
matchDay = input('Quelle journee ? (0 pour derniere journee) : ')

if matchDay :
    url = "https://www.ligue1.fr/calendrier-resultats?seasonId=2019-2020&matchDay="+str(matchDay)

result = requests.get(url, verify=False)
src = result.content

soup = BeautifulSoup(src, 'lxml')
if debug :
    print(soup.prettify())

div = soup.find(class_='container calendar-container-mobile')
#print(div.prettify())

title = soup.find(class_ = 'calendar-widget full-page')
#print(title.div)
week = title.div.contents[2].strip()
#print(week)

container = soup.find(class_='calendar-widget-container')

if debug :
    print(len(container))
    #print(container[0].prettify())
    #print(container)
    #print(list(container.children))
    print('+++++++')
    for i,k in enumerate(container.children):
        print(i,k, type(k))
        print('======================================================================')

#from bs4 import NavigableString, Tag

ul_tags = []
for k in container.children:
    #print('********', k,type(k))
    if  k.name == 'ul':
        ul_tags.append(k)
        #print('********', k,'+++', k.contents[0])
        #ul_tags.append(k.find_all('li'))
        
if debug :
    print(len(ul_tags),ul_tags)

li_tags = []
for k in ul_tags:
    li_tags.append(k.find_all('li'))
        
if debug :
    print(len(li_tags[0]), li_tags[0])        

date_tags = container.find_all(class_='calendar-widget-day')
if debug :
    print(date_tags)
    print(date_tags[0].prettify())

if debug :
    print(date_tags[0])
    #print(ul_tags[0])    
    print(ul_tags[0].prettify())


home = ul_tags[0].find(class_='club home').contents
#print(home)
time = ul_tags[0].find(class_='result').contents
#print(time)
away = ul_tags[0].find(class_='club away').contents
#print(away)

homeid = home[1].find(class_='calendarTeamNameDesktop').contents
#print(homeid)
timeid = time[1].find(class_='lost').contents
#print(timeid)
awayid = away[1].find(class_='calendarTeamNameDesktop').contents
#print(awayid)

def print_all_ul(ul_tags):
    #print(ul_tags[0])
    global week_score, week_data
    
    for k in ul_tags:
        home = k.find(class_='club home').contents
        #print(home)
        ok = True
        time = k.find(class_='result').contents
        timeid = time[1].find(class_='lost').contents[0]
        if 'h' in timeid or 'Rep' in timeid:
            #print(timeid)
            result = timeid
            ok = False
        else:
            span = time[1].find_all('span')
            score1 = span[0].contents
            #print(score1)
            score2 = span[2].contents
            #print(score2)
            result = score1[0]+'-'+score2[0]
            

        away = k.find(class_='club away').contents
        #print(away)
        #for l in range(1, len(home)):
        homeid = home[1].find(class_='calendarTeamNameDesktop').contents
        
        awayid = away[1].find(class_='calendarTeamNameDesktop').contents
        print(result, ': ', homeid[0], ' - ', awayid[0])
        week_score += result+' : '+ homeid[0]+' - '+ awayid[0]+'\n'
        if ok : week_data.append((matchDay, homeid[0], awayid[0], score1[0], score2[0]))

print(week)
#print(container, len(container))
week_data = []
week_score=str(matchDay)
for k in range(len(li_tags)):
    print(date_tags[k].contents[0])
    week_score += date_tags[k].contents[0]+'\n'
    #ul_tags = container.find_all('ul')
    print_all_ul(li_tags[k])
    week_score += '\n'
    print()
#print(week_score)

def to_file(file):
    with open(file,"a") as f:
        f.write(week_score)
import numpy as np        
if save :
    np.save("score"+matchDay,week_data)
    to_file("score"+matchDay+".txt")
    data = np.load("score"+matchDay+".npy")
    print(data)