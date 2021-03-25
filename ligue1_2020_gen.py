#!/usr/bin/env python
# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt

import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup

debug = False

url = "https://www.ligue1.fr/classement?seasonId=2019-2020&matchDay=28"
j=input('Quelle journee ? (0 pour derniere journee) : ')
if j:url = "https://www.ligue1.fr/classement?seasonId=2019-2020&matchDay="+str(j)

result = requests.get(url, verify=False)
src = result.content

soup = BeautifulSoup(src, 'lxml')
if debug :
    print(soup.prettify())

title = soup.find(class_ = 'title')
#print(title.div)
week = title.div.contents[2].strip()
print(week)

page = soup.find(class_='container page-section')
if debug :
    print(page.prettify())

table = page.find(class_='classement-table')
if debug :
    print(table.prettify())

head = table.find(class_='classement-table-head')
#print(head.prettify())

span_head = head.find_all('span')
#for s in span_head:
#    print(s.contents[0], end='\t')

del(span_head[3])
del(span_head[4])
    
if debug :
    print(span_head)

body = table.find(class_='classement-table-body')
#print(body.prettify())

li_tags = body.find_all('li')
#print(len(li_tags), li_tags[1].prettify())


def create_row(position):
    col = li_tags[position].find_all('div')
    row = {}
    for k, c in enumerate(col):
        if k == 10 : break
        content = c.contents[0]
        if k == 1 : content = c.contents[3].find('span').contents[0]
        #print(k, span_head[k].contents[0], content)
        row[span_head[k].contents[0]] = content
    #print(row)
    return row
    
rows = []    
for n in range(20):
    rows.append(create_row(n))
#print(rows)

import pandas as pd
df  = pd.DataFrame.from_dict(rows)
for i in range(2,10):
    #print(df.iloc[:,i])\n",
    df.iloc[:,i]=df.iloc[:,i].astype('int')   # convert to numerical 

print(df[['POSITION','CLUB','POINTS','GAGNÉS','NULS','PERDUS','BUTS POUR', 'BUTS CONTRE','DIFF.']])

# make arrays
position = list(df['POSITION'])
club = list(df['CLUB'])
points = list(df['POINTS'])
g = list(df['GAGNÉS'])
n = list(df['NULS'])
p = list(df['PERDUS'])
bp = list(df['BUTS POUR'])
bc = list(df['BUTS CONTRE'])
diff = list(df['DIFF.'])
#print(list(club))
# save as np.arrays
np.savez_compressed('ligue1_gen.npz', position=position, club=club, points=points, g=g, n=n, p=p, bp=bp, bc=bc, diff=diff)


def autolabel(ax, rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

def draw_stackedbar():
    N = 20
    ind = np.arange(N)    # the x locations for the groups
    width = 0.5       # the width of the bars: can also be len(x) sequence
    p1 = plt.bar(ind, df['GAGNÉS'], width)
    p2 = plt.bar(ind, df['NULS'], width, bottom=df['GAGNÉS'])
    p3 = plt.bar(ind, df['PERDUS'], width, bottom=df['GAGNÉS']+df['NULS'])
    plt.legend((p1[0], p2[0], p3[0]), ('Gagnés', 'Nuls', 'Perdus'))
    plt.show()

def draw_groupedbar(df, cols):
    N = 20
    x = np.arange(N)  # the label locations
    width = 0.3  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width, df[cols[0]], width, label=cols[0])
    rects2 = ax.bar(x , df[cols[1]], width, label=cols[1])
    rects3 = ax.bar(x + width, df[cols[2]], width, label=cols[2])
    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Matchs')
    ax.set_title('Scores')
    ax.set_xticks(x)
    #ax.set_xticklabels(labels)
    ax.legend()
    # label each bar at top
    autolabel(ax, rects1)
    autolabel(ax, rects2)
    autolabel(ax, rects3)
    fig.tight_layout()
    plt.show()

draw_stackedbar()
cols = ('GAGNÉS','NULS','PERDUS')
draw_groupedbar(df, cols)

cols = ('BUTS POUR', 'BUTS CONTRE', 'DIFF.')
draw_groupedbar(df, cols)

result = df.sort_values(by=['BUTS POUR'], ascending=[0])
draw_groupedbar(result, cols)

result = df.sort_values(by=['BUTS CONTRE'], ascending=[0])
draw_groupedbar(result, cols)

result = df.sort_values(by=['DIFF.'], ascending=[0])
draw_groupedbar(result, cols)

def scatter(df,cols,factor=10):
    x = df[cols[0]]
    y = df[cols[1]]
    s, c = np.random.rand(2, 20)
    s = x*factor
    c = x+y
    fig, ax = plt.subplots()
    ax.scatter(x, y, s, c)
    ax.set_ylabel(cols[1])
    ax.set_xlabel(cols[0])
    plt.show()

cols =('BUTS POUR', 'BUTS CONTRE')
scatter(df, cols)

cols =('GAGNÉS', 'PERDUS')
scatter(df, cols, 50)

for i in range(2,10):
    #print(df.iloc[:,i])
    df.iloc[:,i]=df.iloc[:,i].astype('int')
#df.info()

df.to_csv('ligue1_2020_27.csv', sep = ',')
df.describe()
df.set_index('POSITION', drop=True, inplace=True)

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
    
moyenne,variance=moyVar(df.POINTS)
df2 = df[df.POINTS>moyenne]
df2

import numpy as np
import matplotlib.pyplot as plt
l = len(df)
x = np.arange(l)
y = df.POINTS
plt.plot(x,y)
plt.plot(x,np.ones(l)*moyenne)
plt.plot(x,np.ones(l)*variance)
plt.show()