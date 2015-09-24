# q19
# given a random array of int, rearrange it into wave-like array 2 > 1 < 4 > 3 < 6 > 5 ...
# thoughts: sort the array, then skip 2 element and swap a pair
# it sounds too easy to be true, is there any other conditions required for the output? duplicate values?

input = [1, 3, 2, 4, 5, 6, 7, 8]
def q19():
	input.sort()
	for i in xrange(0, len(input) - 1, 2):
		tmp = input[i]
		input[i] = input[i+1]
		input[i+1] = tmp
	print(input)

q19()
