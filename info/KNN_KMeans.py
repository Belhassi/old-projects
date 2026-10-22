from numpy import array,linalg
from numpy.random import randint,seed
from sklearn.cluster import KMeans
from sklearn.neighbors import KNeighborsClassifier
from matplotlib.pyplot import *
###################kmeans###################
seed(4)
x=randint(0,20,(100,2))
m=KMeans(4,random_state=4)
m.fit(x)
C=m.cluster_centers_
L=m.labels_
scatter(x[:,0],x[:,1],c=L)
scatter(C[:,0],C[:,1],c="r",s=200)
show()
#Q1
def initialiser(X, k):
    indices=choice(range(len(X)),k,replace=False)
    return X[indices]
#Q2
def distances(X, C) :
    D=zeros((len(X),len(C)))
    for i in range(len(X)):
        for j in range(len(C)):
            D[i,j]=norm(X[i]-C[j])
    return D
#Q3
def attribue_labels(D):
    return argmin(D,axis=1)
#Q4
def new_centroids(X, oldC, labels):
    newC = oldC.copy()
    for i in range(len(oldC)): 
        p = X[labels == i]
        if len(p) > 0:
            newC[i] = mean(p, axis=0)
        else:
            newC[i] = choice(X)
    return newC
#Q5
def kmeans(X, k, max_iters=100):
    C=initialiser(X, k)
    
    for i in range(max_iters):
        D=distances(X, C)
        L=attribue_labels(D)
        C=new_centroids(X, C, L)
    return C,L
#Q6
def kmeans2(X, k, max_iters=100,tol=10**(-4)):
    C=initialiser(X, k)

    for i in range(max_iters):
        D=distances(X, C)
        L=attribue_labels(D)
        oldC=C.copy()
        C=new_centroids(X, C, L)
        if norm(C-oldC)<tol:
            break
    return C,L
#Q7
#Programme
X=randint(0,20,(30,2))
C,L=kmeans(X, 3)

print(C)
print(L)
C,L=kmeans2(X, 4)
print()
print(L)

#Q8

from matplotlib.pyplot import *
scatter(X[:,0],X[:,1],c=L)
scatter(C[:,0],C[:,1],c="r",marker="x",s=200)

show()

#Q9
for k in range(2,5):
    C,L=kmeans(X, k)
    print(L)


#Q10
from sklearn import cluster 
import matplotlib.pyplot as plt
m = cluster.KMeans(3)
m.fit(X)

print(m.cluster_centers_)
print(m.predict(X))
#Méthode02
C,L=kmeans(X,3)
print(C)
print(L)
from matplotlib.pyplot import *
subplot(211)
scatter(X[:,0],X[:,1],c=L)
scatter(C[:,0],C[:,1],c="r",marker="x",s=200)
subplot(212)
C=m.cluster_centers_
L=m.predict(X)
scatter(X[:,0],X[:,1],c=L)
scatter(C[:,0],C[:,1],c="b",marker="x",s=200)
show()

###################KNN########################"
seed(4)
x=randint(0,20,(30,2))
yr=array([int(a.mean()>=10) for a in x])
m=KNeighborsClassifier(3)
m.fit(x,yr)
print(yr)
yp=m.predict(x)
print(yp)
NE=array([[14,5],[1,5],[14,17]])
print(m.predict(NE))

#Q1
def dist(x1, x2) :
    return linalg.norm(x1,x2)

#Q2
def calculer_distances(x, xtrain) :
    L=[dist(x,a) for a in xtrain]
    return L
#Q3
def trier_par_distance(xtrain, ytrain, x) :
    L=[(xtrain[i],ytrain[i],dist(x,xtrain[i])) for i in range(len(xtrain))]
    return sorted(L,key=lambda c:c[2])
#Q4
def k_voisins(xtrain, ytrain, x, k) :
    L=trier_par_distance(xtrain, ytrain, x)
    return L[:k]
#Q5
def classe_majoritaire(xtrain, ytrain, x, k) :
    kv=k_voisins(xtrain, ytrain, x, k)
    #m=max(kv,key=lambda c:c.count)#
    m=max(kv,key=lambda c:kv.count(c[1]))
    return m[1]
#Q6
def KNN_single(xtrain, ytrain, x, k):
    return classe_majoritaire(xtrain, ytrain, x, k)
#Q7
def KNN_predict(xtrain, ytrain, xtest, k):
    return [KNN_single(xtrain, ytrain, x, k) for x in xtest]
#Q8
def precision(y_true, y_pred):
    cpt=0
    n=len(y_true)
    for i in range(n):
        if y_true[i]==y_pred[i]:
            cpt+=1
    return cpt/n
#Q9
def comparer_k(xtrain, ytrain, xtest, ytest, k_values):
    for k in k_values:
        y_pred=KNN_predict(xtrain, ytrain, xtest, k)
        print("k:",precision(ytest, y_pred))
#Q10
def comparer_sklearn(xtrain, ytrain, xtest, ytest, k=3):
    y_pred1=KNN_predict(xtrain, ytrain, xtest, k)
    m=KNeighborsClassifier(k)
    m.fit(xtrain, ytrain)
    y_pred2=m.predict(xtest)
    return y_pred1-y_pred2
#Q11
"""
"""
from sklearn.datasets import make_blobs
x,y=make_blobs()

m=KNeighborsClassifier(3)
m.fit(x,y)
print(y)
yp=m.predict(x)
print(yp)
print(y-yp)
scatter(x[:,0],x[:,1],c=y)
show()
#Q12
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_blobs
x,y=make_blobs()
xe,xtest,ye,ytest=train_test_split(x,y,test_size=0.2,random_state=42)
m=KNeighborsClassifier()
m.fit(xe,ye)
print(ytest)
yp=m.predict(xtest)
print(yp)
print(ytest-yp)
scatter(x[:,0],x[:,1],c=y)
show()

