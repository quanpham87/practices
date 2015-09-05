# q46
# given 3 sorted linked list, arrange them into 1
# 2 variable, currentNode and nextNode
# pop first node from first list into currentNode, pop first node from other list into nextNode
# if currentNode's value < nextNode's value:
# else 
class Node:
	def __init__(self, val):
		self.value = val
		self.next = None

def q46(n1, n2):
	result = None
	if n1.value < n2.value:
		print(n1.value)
		current = n1
		next = n2
	else:
		print(n2.value)
		current = n2
		next = n1
		
	while current != None and next != None:
		if current.value < next.value:
			if current.next == None:
				print(next.value)
				current = next
				next = next.next
			else:
				if current.next.value < next.value:
					print(current.next.value)
					current = current.next
				else:
					print(next.value)
					temp = current.next
					current = next
					next = temp
		
a = Node(2)
a.next = Node(4)
a.next.next = Node(5)

b = Node(3)
b.next = Node(7)

q46(a, b)