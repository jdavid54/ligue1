import numpy as np
import matplotlib.pyplot as plt

a = {'0': {'POSITION': '1', 'CLUB': 'PARIS SAINT-GERMAIN', 'POINTS': '65', 'JOUÉS': '26', 'GAGNÉS': '21', 'NULS': '2', 'PERDUS': '3', 'BUTS POUR': '71', 'BUTS CONTRE': '24', 'DIFF.': '+47'}, '1': {'POSITION': '2', 'CLUB': 'OLYMPIQUE DE MARSEILLE', 'POINTS': '52', 'JOUÉS': '26', 'GAGNÉS': '15', 'NULS': '7', 'PERDUS': '4', 'BUTS POUR': '36', 'BUTS CONTRE': '25', 'DIFF.': '+11'}, '2': {'POSITION': '3', 'CLUB': 'STADE RENNAIS FC', 'POINTS': '44', 'JOUÉS': '26', 'GAGNÉS': '13', 'NULS': '5', 'PERDUS': '8', 'BUTS POUR': '31', 'BUTS CONTRE': '24', 'DIFF.': '+7'}, '3': {'POSITION': '4', 'CLUB': 'LOSC LILLE', 'POINTS': '43', 'JOUÉS': '26', 'GAGNÉS': '13', 'NULS': '4', 'PERDUS': '9', 'BUTS POUR': '33', 'BUTS CONTRE': '27', 'DIFF.': '+6'}, '4': {'POSITION': '5', 'CLUB': 'AS MONACO', 'POINTS': '39', 'JOUÉS': '26', 'GAGNÉS': '11', 'NULS': '6', 'PERDUS': '9', 'BUTS POUR': '42', 'BUTS CONTRE': '41', 'DIFF.': '+1'}, '5': {'POSITION': '6', 'CLUB': 'RC STRASBOURG ALSACE', 'POINTS': '38', 'JOUÉS': '26', 'GAGNÉS': '11', 'NULS': '5', 'PERDUS': '10', 'BUTS POUR': '32', 'BUTS CONTRE': '29', 'DIFF.': '+3'}, '6': {'POSITION': '7', 'CLUB': 'OLYMPIQUE LYONNAIS', 'POINTS': '37', 'JOUÉS': '26', 'GAGNÉS': '10', 'NULS': '7', 'PERDUS': '9', 'BUTS POUR': '40', 'BUTS CONTRE': '26', 'DIFF.': '+14'}, '7': {'POSITION': '8', 'CLUB': 'STADE DE REIMS', 'POINTS': '37', 'JOUÉS': '26', 'GAGNÉS': '9', 'NULS': '10', 'PERDUS': '7', 'BUTS POUR': '24', 'BUTS CONTRE': '20', 'DIFF.': '+4'}, '8': {'POSITION': '9', 'CLUB': 'MONTPELLIER HÉRAULT SC', 'POINTS': '37', 'JOUÉS': '26', 'GAGNÉS': '10', 'NULS': '7', 'PERDUS': '9', 'BUTS POUR': '32', 'BUTS CONTRE': '29', 'DIFF.': '+3'}, '9': {'POSITION': '10', 'CLUB': 'OGC NICE', 'POINTS': '37', 'JOUÉS': '26', 'GAGNÉS': '10', 'NULS': '7', 'PERDUS': '9', 'BUTS POUR': '38', 'BUTS CONTRE': '36', 'DIFF.': '+2'}, '10': {'POSITION': '11', 'CLUB': 'FC NANTES', 'POINTS': '37', 'JOUÉS': '26', 'GAGNÉS': '11', 'NULS': '4', 'PERDUS': '11', 'BUTS POUR': '28', 'BUTS CONTRE': '28', 'DIFF.': '0'}, '11': {'POSITION': '12', 'CLUB': 'FC GIRONDINS DE BORDEAUX', 'POINTS': '35', 'JOUÉS': '26', 'GAGNÉS': '9', 'NULS': '8', 'PERDUS': '9', 'BUTS POUR': '38', 'BUTS CONTRE': '32', 'DIFF.': '+6'}, '12': {'POSITION': '13', 'CLUB': 'STADE BRESTOIS 29', 'POINTS': '34', 'JOUÉS': '26', 'GAGNÉS': '8', 'NULS': '10', 'PERDUS': '8', 'BUTS POUR': '34', 'BUTS CONTRE': '35', 'DIFF.': '-1'}, '13': {'POSITION': '14', 'CLUB': 'ANGERS SCO', 'POINTS': '33', 'JOUÉS': '26', 'GAGNÉS': '9', 'NULS': '6', 'PERDUS': '11', 'BUTS POUR': '25', 'BUTS CONTRE': '33', 'DIFF.': '-8'}, '14': {'POSITION': '15', 'CLUB': 'AS SAINT-ÉTIENNE', 'POINTS': '29', 'JOUÉS': '26', 'GAGNÉS': '8', 'NULS': '5', 'PERDUS': '13', 'BUTS POUR': '28', 'BUTS CONTRE': '42', 'DIFF.': '-14'}, '15': {'POSITION': '16', 'CLUB': 'FC METZ', 'POINTS': '28', 'JOUÉS': '26', 'GAGNÉS': '6', 'NULS': '10', 'PERDUS': '10', 'BUTS POUR': '24', 'BUTS CONTRE': '34', 'DIFF.': '-10'}, '16': {'POSITION': '17', 'CLUB': 'DIJON FCO', 'POINTS': '27', 'JOUÉS': '26', 'GAGNÉS': '6', 'NULS': '9', 'PERDUS': '11', 'BUTS POUR': '25', 'BUTS CONTRE': '32', 'DIFF.': '-7'}, '17': {'POSITION': '18', 'CLUB': 'NÎMES OLYMPIQUE', 'POINTS': '27', 'JOUÉS': '26', 'GAGNÉS': '7', 'NULS': '6', 'PERDUS': '13', 'BUTS POUR': '26', 'BUTS CONTRE': '39', 'DIFF.': '-13'}, '18': {'POSITION': '19', 'CLUB': 'AMIENS SC', 'POINTS': '23', 'JOUÉS': '26', 'GAGNÉS': '4', 'NULS': '10', 'PERDUS': '12', 'BUTS POUR': '33', 'BUTS CONTRE': '51', 'DIFF.': '-18'}, '19': {'POSITION': '20', 'CLUB': 'TOULOUSE FC', 'POINTS': '13', 'JOUÉS': '26', 'GAGNÉS': '3', 'NULS': '4', 'PERDUS': '19', 'BUTS POUR': '21', 'BUTS CONTRE': '54', 'DIFF.': '-33'}}
#print(a, type(a))
np.savez('/tmp/model.npz', **a)
result = np.load('/tmp/model.npz')
#print(result.files)

rows = [{'POSITION': '1', 'CLUB': 'PARIS SAINT-GERMAIN', 'POINTS': '65', 'JOUÉS': '26', 'GAGNÉS': '21', 'NULS': '2', 'PERDUS': '3', 'BUTS POUR': '71', 'BUTS CONTRE': '24', 'DIFF.': '+47'}, {'POSITION': '2', 'CLUB': 'OLYMPIQUE DE MARSEILLE', 'POINTS': '52', 'JOUÉS': '26', 'GAGNÉS': '15', 'NULS': '7', 'PERDUS': '4', 'BUTS POUR': '36', 'BUTS CONTRE': '25', 'DIFF.': '+11'}, {'POSITION': '3', 'CLUB': 'STADE RENNAIS FC', 'POINTS': '44', 'JOUÉS': '26', 'GAGNÉS': '13', 'NULS': '5', 'PERDUS': '8', 'BUTS POUR': '31', 'BUTS CONTRE': '24', 'DIFF.': '+7'}, {'POSITION': '4', 'CLUB': 'LOSC LILLE', 'POINTS': '43', 'JOUÉS': '26', 'GAGNÉS': '13', 'NULS': '4', 'PERDUS': '9', 'BUTS POUR': '33', 'BUTS CONTRE': '27', 'DIFF.': '+6'}, {'POSITION': '5', 'CLUB': 'AS MONACO', 'POINTS': '39', 'JOUÉS': '26', 'GAGNÉS': '11', 'NULS': '6', 'PERDUS': '9', 'BUTS POUR': '42', 'BUTS CONTRE': '41', 'DIFF.': '+1'}, {'POSITION': '6', 'CLUB': 'RC STRASBOURG ALSACE', 'POINTS': '38', 'JOUÉS': '26', 'GAGNÉS': '11', 'NULS': '5', 'PERDUS': '10', 'BUTS POUR': '32', 'BUTS CONTRE': '29', 'DIFF.': '+3'}, {'POSITION': '7', 'CLUB': 'OLYMPIQUE LYONNAIS', 'POINTS': '37', 'JOUÉS': '26', 'GAGNÉS': '10', 'NULS': '7', 'PERDUS': '9', 'BUTS POUR': '40', 'BUTS CONTRE': '26', 'DIFF.': '+14'}, {'POSITION': '8', 'CLUB': 'STADE DE REIMS', 'POINTS': '37', 'JOUÉS': '26', 'GAGNÉS': '9', 'NULS': '10', 'PERDUS': '7', 'BUTS POUR': '24', 'BUTS CONTRE': '20', 'DIFF.': '+4'}, {'POSITION': '9', 'CLUB': 'MONTPELLIER HÉRAULT SC', 'POINTS': '37', 'JOUÉS': '26', 'GAGNÉS': '10', 'NULS': '7', 'PERDUS': '9', 'BUTS POUR': '32', 'BUTS CONTRE': '29', 'DIFF.': '+3'}, {'POSITION': '10', 'CLUB': 'OGC NICE', 'POINTS': '37', 'JOUÉS': '26', 'GAGNÉS': '10', 'NULS': '7', 'PERDUS': '9', 'BUTS POUR': '38', 'BUTS CONTRE': '36', 'DIFF.': '+2'}, {'POSITION': '11', 'CLUB': 'FC NANTES', 'POINTS': '37', 'JOUÉS': '26', 'GAGNÉS': '11', 'NULS': '4', 'PERDUS': '11', 'BUTS POUR': '28', 'BUTS CONTRE': '28', 'DIFF.': '0'}, {'POSITION': '12', 'CLUB': 'FC GIRONDINS DE BORDEAUX', 'POINTS': '35', 'JOUÉS': '26', 'GAGNÉS': '9', 'NULS': '8', 'PERDUS': '9', 'BUTS POUR': '38', 'BUTS CONTRE': '32', 'DIFF.': '+6'}, {'POSITION': '13', 'CLUB': 'STADE BRESTOIS 29', 'POINTS': '34', 'JOUÉS': '26', 'GAGNÉS': '8', 'NULS': '10', 'PERDUS': '8', 'BUTS POUR': '34', 'BUTS CONTRE': '35', 'DIFF.': '-1'}, {'POSITION': '14', 'CLUB': 'ANGERS SCO', 'POINTS': '33', 'JOUÉS': '26', 'GAGNÉS': '9', 'NULS': '6', 'PERDUS': '11', 'BUTS POUR': '25', 'BUTS CONTRE': '33', 'DIFF.': '-8'}, {'POSITION': '15', 'CLUB': 'AS SAINT-ÉTIENNE', 'POINTS': '29', 'JOUÉS': '26', 'GAGNÉS': '8', 'NULS': '5', 'PERDUS': '13', 'BUTS POUR': '28', 'BUTS CONTRE': '42', 'DIFF.': '-14'}, {'POSITION': '16', 'CLUB': 'FC METZ', 'POINTS': '28', 'JOUÉS': '26', 'GAGNÉS': '6', 'NULS': '10', 'PERDUS': '10', 'BUTS POUR': '24', 'BUTS CONTRE': '34', 'DIFF.': '-10'}, {'POSITION': '17', 'CLUB': 'DIJON FCO', 'POINTS': '27', 'JOUÉS': '26', 'GAGNÉS': '6', 'NULS': '9', 'PERDUS': '11', 'BUTS POUR': '25', 'BUTS CONTRE': '32', 'DIFF.': '-7'}, {'POSITION': '18', 'CLUB': 'NÎMES OLYMPIQUE', 'POINTS': '27', 'JOUÉS': '26', 'GAGNÉS': '7', 'NULS': '6', 'PERDUS': '13', 'BUTS POUR': '26', 'BUTS CONTRE': '39', 'DIFF.': '-13'}, {'POSITION': '19', 'CLUB': 'AMIENS SC', 'POINTS': '23', 'JOUÉS': '26', 'GAGNÉS': '4', 'NULS': '10', 'PERDUS': '12', 'BUTS POUR': '33', 'BUTS CONTRE': '51', 'DIFF.': '-18'}, {'POSITION': '20', 'CLUB': 'TOULOUSE FC', 'POINTS': '13', 'JOUÉS': '26', 'GAGNÉS': '3', 'NULS': '4', 'PERDUS': '19', 'BUTS POUR': '21', 'BUTS CONTRE': '54', 'DIFF.': '-33'}]
'''
à voir plus tard
np.savetxt('ligue1_rows.txt', dict(rows))
npfile = np.load('ligue1_rows.txt')
print(npfile)
'''
#save dict rows
d = {}
for k in range(20):
    d[str(k)]= rows[k]
#print(d, type(d))

np.savez('ligue1_dict.npz', **d)

def create_data(filename):
    npzfile = np.load(filename)
    print('npzfile',type(npzfile), npzfile.files)
    data = {}
    for k in npzfile.files:    
        data[k] = npzfile[k].item()   # npzfile[k] type ndarray, npzfile[k].item() type dict
        #print(k,npzfile[k], type(npzfile[k]),type(data[k]))
        #data.append(result[k])
    print('data',data)
    return data

data = create_data('ligue1_dict.npz')

import pandas as pd

df  = pd.DataFrame.from_dict(data, orient='index')
print('df=',df)

for i in range(2,9):
    #print(df.iloc[:,i])\n",
    df.iloc[:,i]=df.iloc[:,i].astype('int')   # convert to numerical 

print(df[['POSITION','CLUB','POINTS','GAGNÉS','NULS','PERDUS','BUTS POUR', 'BUTS CONTRE','DIFF.']])


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
'''
result = df.sort_values(by=['BUTS CONTRE'], ascending=[0])
draw_groupedbar(result, cols)

result = df.sort_values(by=['DIFF.'], ascending=[0])
draw_groupedbar(result, cols)
'''
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

# le fichier npz est généré par ligue1_2020_gen.py
npzfile2 = np.load('ligue1_gen.npz')
print('npzfile2',type(npzfile2), npzfile2.files)
df  = pd.DataFrame.from_dict(npzfile2, orient='index')
print(df)
df = df.T
print(df)

for i in range(2,9):
    #print(df.iloc[:,i])\n",
    df.iloc[:,i]=df.iloc[:,i].astype('int')   # convert to numerical

print(df.info())
df.set_index('position', inplace=True)
print(df)

# add column with computed values
df['Pts/J']=df.iloc[:,1]/df.iloc[:,2]
df['Bp/J']=df.iloc[:,6]/df.iloc[:,2]
df['Bc/J']=df.iloc[:,7]/df.iloc[:,2]
print(df)

cols = ('bp', 'bc', 'diff')
draw_groupedbar(df, cols)

cols =('Bp/J', 'Bc/J',500)
scatter(df, cols)
