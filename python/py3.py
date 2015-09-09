def productFib(prod):
    f = [0, 1]
    while (f[-1] * f[-2] < prod):
        f.append(f[-1] + f[-2])
    return [f[-2], f[-1], f[-2] * f[-1] == prod]
