import numpy as np
import numpy.linalg as alg


##esperance
N = 10000
n = 5

L = []
for i in range(N):
    M = 2*np.random.randint(0,2, (n,n)) - 1
    L.append(alg.det((M)))
E = np.mean(L)

##variance

V = np.var(L)