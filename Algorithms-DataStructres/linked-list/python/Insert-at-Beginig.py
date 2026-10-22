class Node(object):
	def __init__(self, Data):
		super(Node, self).__init__()
		self.Data = Data
		self.next = None

class SNode(object):
	def __init__(self):
		self.HeadVal = None

head = SNode()

def PrintValues():
	global head
	temp = head.HeadVal

	while temp is not None:
		print(temp.Data, end=" ")
		temp = temp.next
	print("\n")

def Insert(data):
	global head
	NewNode = Node(data)

	if head.HeadVal is None:
		head.HeadVal = NewNode
	
	else:
		NewNode.next = head.HeadVal
		head.HeadVal = NewNode

def main():
	loop = int(input("Who Many number: "))

	for i in range(loop):
		Data = int(input("Enter the Number: "))

		Insert(Data)
		PrintValues()

if __name__ == '__main__':
	main()
