class Node(object):
	def __init__(self, Data):
		super(Node, self).__init__()
		self.Data = Data
		self.next = None

class SNode(object):
	def __init__(self):
		self.HeadVal = None

def PrintValues():
	temp = head.HeadVal

	while temp is not None:
		print(temp.Data, end=" ")
		temp = temp.next
	print("\n")

def Insert(data, pos):
	NewNode = Node(data)

	if pos == 1:
		NewNode.next = head.HeadVal
		head.HeadVal = NewNode
	
	else:
		temp = head.HeadVal

		

head = SNode()
def main():
	Insert(2, 1)
	PrintValues()

	Insert(3, 2)
	PrintValues()

	Insert(66, 1)
	PrintValues()

	Insert(5, 4)
	PrintValues()