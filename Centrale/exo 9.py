import numpy as np
import numpy.linalg as alg
import matplotlib.pyplot as plt


def construire(n, a):
    A = np.eye(n)

    for i in range(0, n-1):
        A[i, i+1] = -1
        A[i+1, i] = a(i+1)

    return A

def delta(n, a):
    M = construire(n, a)
    return alg.det(M)

f1 = lambda x: 1
f2 = lambda x: 1/(x**2)

t = np.arange(1, 500)
y = [delta(n, f2) for n in t]

plt.scatter(t, y)
plt.show()
