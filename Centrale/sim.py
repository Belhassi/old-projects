import numpy as np
import numpy.linalg as alg
import matplotlib.pyplot as plt


def M(n, t):
    M = np.zeros((n,n))

    for j in range(n):
        for i in range(n-j):
            M[i][j] = 1

    M[n-1][n-1] = t
    return M

def vp(n, t):
    vp = alg.eigvals(M(n,t))
    return np.sort(vp)

def det(n, t):
    return alg.det(M(n,t))


n = 3
t = np.linspace(-100, 100 , 1000)
A, B, C, D = [], [] ,[], []
for x in t:
    temp = vp(n, x)
    A.append(temp[0])
    B.append(temp[1])
    C.append(temp[2])
    D.append(det(n, x))
plt.plot(t, A, label='alpha')
plt.plot(t, B, label='beta')
plt.plot(t, C, label='gama')
#plt.plot(t, D)
plt.grid()
plt.legend()
plt.show()
