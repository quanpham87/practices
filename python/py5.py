# q17
# given the assumption that start time is continuous, there's no need to bubbling
# start top down, if i start time overlaps i - 1 start time then it needs its own ram
# otherwise get max(i's ram, i - 1's ram, currentMax)
input = [[2, 4, 1], [3, 6, 2], [3, 9, 3], [8, 11, 5]]

def q17():	
	maxRam = input[0][2]
	maxEndTime = input[0][1]
	for i in range(1, len(input)):
		if input[i][0] < maxEndTime:
			maxRam += input[i][2]
		else:
			maxRam = max(input[i][2], maxRam)
		maxEndTime = max(maxEndTime, input[i][1])
	print(maxRam)
	
q17()

# in the solution they use tree mapping, I don't know what that is but the speed is O(NlogN)
# my solution speed is O(N), shouldn't it be faster?
# need more test cases
