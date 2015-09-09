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
