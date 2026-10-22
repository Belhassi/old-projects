import numpy as np
import matplotlib.pyplot as plt
import math

##1
N = 1000
t = np.linspace(0, 25 , N)
#y = np.array([math.sin(x) for x in t])
y_sin = np.sin(t)
plt.plot(t, y_sin, label='sin')

##2
y_cos = np.cos(t)
y_sum = y_sin + y_cos

plt.plot(t, y_cos, label='cos')
plt.plot(t, y_sum, label='sin + cos')
plt.legend()
plt.title('differents fonctions')
plt.grid()

plt.show()