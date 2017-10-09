
import numpy as np

def getb4(i):
    length=(bin(i)+"").replace("0b","").__len__()
    if length<=4:
        return "0000"[length:4]+(bin(i)+"").replace("0b","")
    if length> 4:
        return (bin(i)+"").replace("0b","")[length-4:length]

def getb8(i):
    length=(bin(i)+"").replace("0b","").__len__()
    print length
    if length<=8:
        return "00000000"[length:8]+(bin(i)+"").replace("0b","")
    if length> 8:
        return (bin(i)+"").replace("0b","")[length-8:length]

print np.array([int(x) for x in list(getb8(12))])




print hex(ord("a"))



# sigmoid function
def nonlin(x,deriv=False):
    if(deriv==True):
        return x*(1-x)
    return 1/(1+np.exp(-x))

# input dataset
X = np.array([  [0,0,1],
                [0,1,1],
                [1,0,1],
                [1,1,1] ])

# output dataset
y = np.array([[0,0,1,1]]).T

# seed random numbers to make calculation
# deterministic (just a good practice)
np.random.seed(1)

# initialize weights randomly with mean 0
syn0 = 2*np.random.random((3,1)) - 1

for iter in xrange(10000):
    # forward propagation
    l0 = X
    l1 = nonlin(np.dot(l0,syn0))

    # how much did we miss?
    l1_error = y - l1

    # multiply how much we missed by the
    # slope of the sigmoid at the values in l1
    l1_delta = l1_error * nonlin(l1,True)

    # update weights
    syn0 += np.dot(l0.T,l1_delta)
print "Output After Training:"
print l1
