from np import updatedata
def run(id=id):
    import imp
    fp, pathname, description = imp.find_module("cell"+str(id))

    try:
        m = imp.load_module("cell"+str(id), fp, pathname, description)
        print m.getoutput()
        m.updateinput()
        print m.getoutput()
    finally:
        if fp:
            fp.close()
def getOutput(id=id):
    import imp
    fp, pathname, description = imp.find_module("cell"+str(id))
    try:
        m = imp.load_module("cell"+str(id), fp, pathname, description)
        return m.getoutput()
    finally:
        if fp:
            fp.close()
def runall():
    for i in range(10):
        print 'cell:',9-i
        run(9-i)


import pandas as pd
name='data1'
data = pd.read_csv(name+'.csv',sep=',',encoding='gbk')
datalist= data.values.tolist()

# for i in range(10):
#     updatedata.updaterandom(i)

runall()
# for i in range(20):
#     runall()
