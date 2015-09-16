# Q16
input = [[1, 1, 2], [1, 3, 2], [2, 2, 2]]
m = 2
n = 2
target = input[m][n]

def findArea(n, i, j):
	# recursion fails because when we go to i + 1 and it tries to go back to i - 1 => i => infinite loop
	# if (i < 0 or i > 2 or j < 0 or j > 2 or n != input[i][j]):
		# return 0
	# else:
		# #return 1 + findArea(n, i - 1, j) + findArea(n, i + 1, j) + findArea(n, i, j - 1) + findArea(n, i, j - 1)
		# return 1 + findArea(n, i + 1, j) + findArea(n, i - 1, j)
		
	# switch to queue
	# THIS IS SO BAAAAD but at least I got it done, will revisit for a better algorithm
	queue = [[i, j]]	
	bqueue = [[i, j]]
	area = 0
	
	def inRange(h, x):
		if (x in range(0, h)):
			return True
		return False
		
	while (True):
		v = queue.pop()
		area += 1
		if (inRange(3, v[0] + 1) and inRange(3, v[1]) and input[v[0] + 1][v[1]] == n and [v[0] + 1, v[1]] not in bqueue):
			queue.append([v[0] + 1, v[1]])
			bqueue.append([v[0] + 1, v[1]])
			
		if (inRange(3, v[0] - 1) and inRange(3, v[1]) and input[v[0] - 1][v[1]] == n and [v[0] - 1, v[1]] not in bqueue):
			queue.append([v[0] - 1, v[1]])
			bqueue.append([v[0] - 1, v[1]])
			
		if (inRange(3, v[1] + 1) and inRange(3, v[0]) and input[v[0]][v[1] + 1] == n and [v[0], v[1] + 1] not in bqueue):
			queue.append([v[0], v[1] + 1])
			bqueue.append([v[0], v[1] + 1])
			
		if (inRange(3, v[1] - 1) and inRange(3, v[0]) and input[v[0]][v[1] - 1] == n and [v[0], v[1] - 1] not in bqueue):
			queue.append([v[0], v[1] - 1])
			bqueue.append([v[0], v[1] - 1])
		
		if (len(queue) == 0):
			return area
		
print(findArea(target, m, n))
