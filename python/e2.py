# q50
# given an undirected graph, copy the whole structure

class Node:
	def __init__(self, val):
		self.value = val
		self.neighbors = []
		
# this is a graph, so can either use BFS or DFS
def getNode(original):
	newNode = Node(original.value)
	for adj in original.neighbors:
		newNode.neighbors.append(getNode(adj))
	return newNode


a = Node("Test")
a.neighbors.extend([Node("one"), Node("two")])

print(a.value)
print(a.neighbors)

b = getNode(a)
print(b.value)
print(b.neighbors)

a.value = "new value"
print(a.value)
print(b.value)