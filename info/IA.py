from numpy.random import choice, randint, seed
from numpy import zeros, argmin, mean, array
from numpy.linalg import norm
from matplotlib.pyplot import *

from sklearn.cluster import KMeans
from sklearn.neighbors import KNeighborsClassifier

seed(4)
X = randint(0,21,(200, 2))
#X[:,0]=range(200)
##Q1
def initialiser(X,k):
    indices =  choice(range(len(X)), k, replace=False)
    return X[indices]


##Q2
def distance(X, centroids):
    D = zeros((len(X), len(centroids)))

    for i in range(len(X)):
        for j in range(len(centroids)):
            D[i,j] = norm(X[i]-centroids[j])
    return D

##Q3
def attribue_labels(D):
    return argmin(D,axis=1)

##Q4
def new_centroids(X, OldC, labels):
    Nc = OldC.copy()
    for i in range(len(OldC)):
        p = X[labels == i]
        if len(p)!=0:
            Nc[i] = mean(p, axis=0)
    return Nc

##Q5
def kmeans(X, k, mx_it=1000, e=10**-5):
    C = initialiser(X,k)
    for i in range(mx_it):
        oldC = C.copy()
        D = distance(X, C)
        L = attribue_labels(D)
        C = new_centroids(X, C, L)
        if norm(oldC-C)<e:
            break
    return C,L

##Q8
def graph(X):
    C,L = kmeans(X,2)
    scatter(X[:,0], X[:,1], c=L)
    scatter(C[:,0], C[:,1], c='r', marker='x', s=200)
    show()

##Q10
def B_KMN(X, k):
    m = KMeans(k,random_state=4)
    m.fit(X)
    C = m.cluster_centers_
    L = m.labels_
    scatter(X[:,0], X[:,1], c=L)
    scatter(C[:,0], C[:,1], c='r', marker='x', s=200)
    show()

def KNN(X):
    Y = array([int(a.mean()>=10)] for a in X)
    m = KNeighborsClassifier()
    m.fit(X, Y)
    print(yr)

    yp = m.predict(X)
    print(yp)
    NE = array([[18, 15]])
    print(m.predicgt(NE))










    
