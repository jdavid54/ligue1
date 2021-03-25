#print(data,len(data))
import numpy as np
import pandas as pd
df = pd.read_csv('ligue1_csv')
#print(df)

df.set_index('Position', drop=True, inplace=True)
print('d',df)
#df.info()  #pas besoin de convertir en int
'''
#convert columns str to int
for i in range(1,9):
    #print(df.iloc[:,i])
    df.iloc[:,i]=df.iloc[:,i].astype('int') 

df['Pts/J']=df.iloc[:,1]/df.iloc[:,2]
df['Bp/J']=df.iloc[:,6]/df.iloc[:,2]
df['Bc/J']=df.iloc[:,7]/df.iloc[:,2]
print('f',df)

print('h',df.describe())

print('i',df.describe().loc['mean'])

print('j',df.describe().loc[['mean','std']])

print('k',df.describe().columns)
print('l')
df.info()

empirique = True
if empirique == True :
    n -= 1
'''
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
        v = s2/n - m**2
        ve = v*n/(n-1)
        e_type = np.sqrt(ve)
        return m, v, ve, e_type   # moyenne, var, var empirique, ecart_type

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

def moyDist(X):
    n = len(X)
    moyenne, variance, ve, e_type = moyVar(X)
    D = []
    for x in X:
        D.append(x-moyenne)
    print(D)
    D2 = [k**2 for k in D]
    var = sum(D2)/(n-1)    # empirique
    ecart_type = np.sqrt(var)
    return var, variance, D, D2 , ecart_type

print(moyVar(df.Pts))
#print(moyVar(df['Pts/J']))
#print(moyVarP(df.Pts,df['Pts/J']))

for k in range(1,12):
    print(df.columns[k],moyVar(df.iloc[:,k]),df.iloc[:,k].var())
    

v = moyDist(df.Pts)

'''
print(df[df.Pts>moyenne])
print(df[df.Pts<moyenne])
'''
import numpy as np
import matplotlib.pyplot as plt
l = len(df)
x = np.arange(l)
y = df.Pts
moyenne,variance, ve, e_type = moyVar(y)
plt.title('Stats Pts')
plt.plot(x,y)
plt.plot(x,np.ones(l)*moyenne,label='moyenne')    # df.mean()
plt.plot(x,np.ones(l)*ve,label='variance')        # df.var()
plt.plot(x,np.ones(l)*e_type,label='ecart-type')  # df.std()

plt.grid()
plt.legend()
plt.show()

plt.bar(x,v[2])
plt.bar(x,v[3])
plt.title('Variance, ecart_type')
plt.show()

# répartition des points
print(df.Pts)
df.Pts.plot.hist()
plt.title('Histogramme Pts')
plt.show()

df['Diff.'].plot.hist()
plt.title('Histogramme Diff.')
plt.show()

df['Bp'].plot.hist()
plt.title('Histogramme Bp')
plt.show()

# classement par valeurs décroissantes de Bc,Bp, Diff.
bc = df.sort_values('Bc',ascending=False)
bp = df.sort_values('Bp',ascending=False)
diff = df.sort_values('Diff.',ascending=False)
print(bc.iloc[:,:9])
print(bp.iloc[:,:9])
print(diff.iloc[:,:9])


df.plot.scatter(x='Pts', y='Bp')
plt.title('Corrélation Pts/Buts pour')
plt.show()

df.plot.scatter(x='Pts', y='Diff.')
plt.title('Corrélation Pts/Différence Buts')
plt.show()

df.plot.scatter(x='Pts', y='Bc')
plt.title('Corrélation Pts/Buts contre')
plt.show()