import numpy as np
import numpy.linalg as alg

##2
A = np.array([[1,2],[3,4]])
I = np.eye(2)

print(alg.matrix_power(A,5))

##3
det = alg.det(A)
rg = alg.matrix_rank(A)
A_inv = alg.inv(A)

##4
B = np.array([1,5])
X = alg.solve(A, B)

##5
val_p = np.linalg.eigvals(A)
vect_p = np.linalg.eig(A)[1]

