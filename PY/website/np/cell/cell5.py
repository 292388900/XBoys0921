id=5
output=0
import numpy as np
def getinput(id=id):
    import imp
    fp, pathname, description = imp.find_module("data"+str(id))

    try:
        m = imp.load_module("data"+str(id), fp, pathname, description)
        return m.input
    finally:
        if fp:
            fp.close()
def getweight(id=id):
    import imp
    fp, pathname, description = imp.find_module("data"+str(id))

    try:
        m = imp.load_module("data"+str(id), fp, pathname, description)
        return m.weight
    finally:
        if fp:
            fp.close()
def getconnect(id=id):
    import imp
    fp, pathname, description = imp.find_module("data"+str(id))

    try:
        m = imp.load_module("data"+str(id), fp, pathname, description)
        return m.connect
    finally:
        if fp:
            fp.close()

def getoutput(id=id):
    s=0
    input=getinput(id=id)
    weight=getweight(id=id)
    for x in range(len(input)):
        s+=input[x]*weight[x]
    output= 1/(1+np.exp(-s))
    return output

connect=getconnect()
if len(connect)==0:
    print output
    print 'end'

def run(id=id):
    import imp
    fp, pathname, description = imp.find_module("cell"+str(id))

    try:
        m = imp.load_module("cell"+str(id), fp, pathname, description)
        return m.getoutput()
    finally:
        if fp:
            fp.close()
def updateinput(id=id):
    input=[]
    for cell in connect:
        input.append(run(cell))
    from np import updatedata
    updatedata.update(id=id,key='input',value=input)
