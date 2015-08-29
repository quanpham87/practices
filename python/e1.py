print "Learning Python the Hard Way"

# for taking arguments from command line
from sys import argv
# # starts a comment line

print "multiple objects in one line", 10, "more text"

myName = "Quan Pham"
# use %% to escape % symbol, use \ to escape other special characters
# put parameters in ( ) if printing multiple of them
print 'user percentage (%%) symbol to format string: %s' % myName

# assign multiple parameters at once
# this is called unpacking, it can apply to function too
a, b, c, d = 1, 2, 3,4
print a, b, c, d

def testUnpacking():
    """ This is for documenting, not commenting, like the summary section in c# """
    return 1, 2, 3, 4
e, f, g, h = testUnpacking()
print e, f, g, h

# pop(0) => 1st, pop(-1) => last

if 1 == 1:
    print "True"
    
print "Outside of if"

# classes need to implement object class
class Car(object):
    pass

class Sedan(Car):
    def __init__(self):
        self.doors = 4
    def toString(self):
        print "Has %i doors" % self.doors
        
x = Sedan()
x.toString()

try:
    print "try catch"
except Error:
    print "error"