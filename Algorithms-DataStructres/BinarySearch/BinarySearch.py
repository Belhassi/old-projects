import random

def Search(arr, target):
	start = 0
	End = len(arr) - 1

	for i in range(len(arr)):
		mid = (start+End)//2

		if arr[mid] == target:
			return mid
		elif arr[mid] > target:
			End = mid
		else:
			start = mid+1
	return 0

array = sorted(random.sample(range(1, 100), 99))
search = Search(array, int(input("Enter the Number :")))

if search:
	print("it is in the index : ", search)
else:
	print("Not found")