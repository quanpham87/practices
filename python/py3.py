def productFibV2(prod):
    f = [0, 1]
    while (f[-1] * f[-2] < prod):
        f.append(f[-1] + f[-2])
    return [f[-2], f[-1], f[-2] * f[-1] == prod]
    
def productFib(prod):
    a, b = 0, 1
    while (a * b < prod):
        a, b = b, a + b
    return [a, b, a * b == prod]

import math

def isPP(n):
    #your code here
    i = 2
    while (i <= math.sqrt(n)):        
        count = 1
        while (i**count < n):
            count += 1
        if (i**count == n):
            return [i, count]
        i += 1
