# q45
# reverse an integer without using any built-in functions
# signed or unsigned, integer => no decimal point

def reverse(input):
    print("--Q45--")
    # check for sign
    neg = False
    if (input < 0):
        neg = True
        
    input = abs(input)
    out = 0
    while (input / 10 > 0):    
        out += (input % 10) * pow(10, len(str(input)) - 1)
        # alternate way:
        # out = (out * 10) + (input % 10)
        input = input / 10
    out += input % 10
    if neg:
        out = out * -1
    print out
    
reverse(123)
reverse(-123)

# q44
# add 2 binary # that is stored as array
def addBin(n1, n2):
    print("--Q44--")
    carry = 0
    out = ""
    while (len(n1) > 0 or len(n2) > 0):
        b1 = n1.pop(-1)
        b2 = n2.pop(-1)
        if b1 != b2:
            if carry == 0:
                out = "1" + out
            else:
                out = "0" + out
        else:
            if carry == 0:
                out = "0" + out
            else:
                out = "1" + out
                carry = 0
            if b1 == 1:
                carry = 1
    print(out)
    
addBin([0, 0, 1], [1, 0, 1])