# improved fib function by using a cache
cache = {}
def fibonacci(n):
	if n in [0, 1]:
		return n
	else:
		if str(n) in cache.keys():
			return cache[str(n)]
		else:
			o = fibonacci(n-1) + fibonacci(n-2)
			cache[str(n)] = o
			return o
	
# for i in range(10):
	# print(fibonacci(i))
	
	
def valid_parentheses(string):
    s = []
    for i in string:
        if i == '(':
            s.append(i)
        elif i == ')':
            if len(s) == 0:
                return False
            s.pop()
    if len(s) == 0:
        return True
        
    return False
	
	
# in progress
def is_merge(s, part1, part2):
	print(part1 + " : " + part2)
	m = 0
	n = 0
    
	for i in s:
        # if part1 current location match => pass
        # if part2 current location match => pass
		print(m)
		print(n)
		print('---')
		if m == len(part1) & n == len(part2):
			return False
            
		if part1[m] == i:
			m += 1
		elif part2[n] == i:
			n += 1
		else:
			return False
	if m != len(part1) | n != len(part2):
		return False
	return True
	
print(is_merge('codewars', 'code', 'code'))
