def prefill(n,v=None):
    if (not str(n).isdigit()):
        raise TypeError("%s is invalid" % str(n))
    elif (int(n) == 0):
        return []
    else:
        if (v == None):
            v = 'undefined'
        out = []
        out.extend(getList(int(n), v))
        return out
        
def getList(n, v):
    if (n == 1):
        return [v]
        
    t = [v]
    t.extend(getList(n-1, v))
    return t
