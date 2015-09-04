# q50
# given an undirected graph, copy the whole structure

class Node:
	def __init__(self, val):
		self.value = val
		self.neighbors = []
		
# this is a graph, so can either use BFS or DFS
# speed O(n), space O(1)
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

# q48
# very good mental challenge question:
# given an array of length k, find the missing value knowing that all the other values (from 1 to k) are in the array
# solution: because the values are from 1 to k and no duplication => sum of all = (1 + k) * k/2. Now we calculate the sum of the array and the remaining is the missing value
# speed O(N), space O(1)
def findMissingValue(arr):
	sum = 0
	for i in arr:
		if (i != None):
			sum += i
	theoreticalSum = (1 + len(arr)) * len(arr)/2
	return theoreticalSum - sum

print(findMissingValue([4, 1, 3, 5, None]))
print(findMissingValue([4, 1, 3, 2, None]))

# q47
# from a list of words, write out each line words that are anagram
# solutions: go through each word, break the word into dictionary of character, see if we can build other words out of it then add the word and the list of anagrams to another dictionary for display
# if a word  is already an anagram of other words then skip it
print("--Q47--")
def canConstruct(chars, word):
	for c in word:
		if c not in chars:
			return False
		else:
			chars[c] -= 1
	for c in chars:
		if chars[c] != 0:
			return False
	return True
	
def q47():
	skip = []
	words = ["abc", "hello", "cba"]
	out =  {}
	for i in range(len(words)):
		w = words[i]
		if w not in skip:
			out[w] = [w]
			chars = {}
			for c in w:
				if chars.has_key(c):
					chars[c] += 1
				else:
					chars[c] = 1
			for j in range(i+1, len(words)):
				if canConstruct(chars, words[j]):
					out[w].append(words[j])
					skip.append(words[j])
	print(out)
	
q47()

# z = { 'a': 1, 'b': 2 }
# for c in z:
	# print(c)
# print(1 in z)