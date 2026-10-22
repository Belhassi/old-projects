from numpy.random import choice, randint, seed
from numpy import zeros, argmin, mean, array
from numpy.linalg import norm
from matplotlib.pyplot import *

from sklearn.cluster import KMeans
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import make_blobs


##Q1
def dist(x1, x2):
    return linalg.norm(x1-x2)

##Q2
def calculer_distnaces(x, Xtrain):
    return [dist(x, a) for a in Xtrain]

##Q3
def trier_par_distance(xtrain, ytrain, x):
    L = [(xtrain[i], ytrain[i], distances(x, xtrain[i])) for i in range(len(x))]
    return sorted(L, key=lambda a: a[2])

##Q4
def k_voisins(xtrain, ytrain, x, k):
    L = trier_par_distance()
    return L[:k]
    
##Q5
def classe_majoritaire(xtrain, ytrain, x,k):
    L = k_voisins(xtrain, ytrain, x,k)
    m = max(L, key=lambda x:L.count(x[1]))
    return m[1]

##Q6
def KNN_single(xtrain, ytrain, x, k):
    return classe_majoritaire(xtrain, ytrain, x, k)

##Q7
def KNN_predict(xtrain, ytrain, xtest, k):
    return [KNN_single(xtrain, ytrain, x, k) for x in xtest]

##Q8
def precision(ytrue, ypred):
    cpt = 0
    for i in range(ytrue):
        if ytrue[i] == ypred[i]:
            cpt += 1
    return cpt/len(ytrue)

##Q9
def copmparer_k(xtrain, ytrain, xtest, ytest, k_values):
    for k in k_values:
        y_pred = KNN_predict(xtrain, ytrain, xtest, k)
        print(k,' ', precision(yest, y_pred))

##Q10
def copmparer_knn(xtrain, ytrain, xtest, ytest, k=3):
    y_pred1 = KNN_predict(xtrain, ytrain, xtest, k)
    m = KNeighborsClassifier(k)
    m.fit(xtrain, ytrain)
    y_pred2 = predict(xtest)
    return y_pred1-ypred2

##Q11

x,y = make_blobs()
yp = KNN_predict(x, y, xtest, 5)
print(y-yp)
scatter(x[:,0], x[:,1])
show()






























