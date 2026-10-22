class Node(object):
	def __init__(self, Data):
		super(Node, self).__init__()
		self.Data = Data
		self.next = None

class SNode(object):
	def __init__(self):
		super(SNode, self).__init__()
		self.HeadVal = None
		

def PrintAll(Head):
	temp = Head.HeadVal

	while temp is not None:
		print(Val.Data, end=" ")
		temp = temp.next
	print("\n")

def Insert(Data):

	NewNode = Node(Data)
	if head.HeadVal is None:
		head.HeadVal = NewNode
		return

	temp = head.HeadVal
	while(temp.next):
		temp = temp.next

	temp.next = NewNode


head = SNode()

n = int(input("Who Many number: "))

for i in range(n):
	Data = int(input("Enter the Number: "))

	Insert(Data)
	PrintAll(head)