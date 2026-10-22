import numpy as np

def sort(array):
	while True:
		counter = 0
		for i in range(len(array)):
			if i == 0:
				continue

			if array[i] < array[i-1]:
				val = array[i]
				array[i] = array[i-1]
				array[i-1] = val 

				counter += 1
		if not counter:
			return array

array = list(np.random.random_integers(10, size=(1,1000)))[0]
print(array)
# print(sort(array))