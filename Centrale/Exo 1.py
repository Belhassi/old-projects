import numpy as np


##1
A = np.array([
            [1,2,3],
            [4,5,6],
            [7,8,9]
])

##2
l2 = A[1]
c3 = A[:,2]
m = A[1:,1:]

##4
I4 = np.eye(4)
B = np.zeros((3,5))
D = np.diag((1,5,-1)



##5
I3 = I4[:3,:3]
M1 = np.concatenate((I3, A), axis=0)
M2 = np.concatenate((A, I3), axis=0)
M = np.concatenate((M1, M2), axis=1)


