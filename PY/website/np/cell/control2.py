from np import updatedata
def run(id=id):
    import imp
    fp, pathname, description = imp.find_module("cell"+str(id))

    try:
        m = imp.load_module("cell"+str(id), fp, pathname, description)
        # print m.getoutput()
        m.updateinput()
        # print m.getoutput()
    finally:
        if fp:
            fp.close()
def runall():
    for i in range(10):
        run(9-i)

def getOutput(id=id):
    import imp
    fp, pathname, description = imp.find_module("cell"+str(id))
    try:
        m = imp.load_module("cell"+str(id), fp, pathname, description)
        return m.getoutput()
    finally:
        if fp:
            fp.close()

import pandas as pd
name='data1'
data = pd.read_csv(name+'.csv',sep=',',encoding='gbk')
datalist= data.values.tolist()

resultlist=[]
resultlistx=[]
resultlisty=[]

# print getOutput(9),getOutput(8),getOutput(7),getOutput(6),getOutput(5),getOutput(4),getOutput(3),getOutput(2),getOutput(1),getOutput(0)
# updatedata.update(10,key='input',value=datalist[12])
# print getOutput(9),getOutput(8),getOutput(7),getOutput(6),getOutput(5),getOutput(4),getOutput(3),getOutput(2),getOutput(1),getOutput(0)
# updatedata.update(10,key='input',value=datalist[13])
# runall()
# print getOutput(9),getOutput(8),getOutput(7),getOutput(6),getOutput(5),getOutput(4),getOutput(3),getOutput(2),getOutput(1),getOutput(0)

for k in range(119):
    for i in range(10,12):
        updatedata.update(i,key='input',value=datalist[k])
    for j in range(10):
        runall()
    resultlistx.append(getOutput(8))
    resultlisty.append(getOutput(9))
    resultlist.append(getOutput(8)/getOutput(9))
resultlistset=list(set(resultlist))
print resultlistset
from matplotlib import pyplot as plt
axes = plt.subplot(111)

datalist0x=[]
datalist1x=[]
datalist2x=[]
datalist3x=[]
datalist0y=[]
datalist1y=[]
datalist2y=[]
datalist3y=[]
i=0
for dl in datalist:
    if resultlist[i]==resultlistset[0]:
        datalist0x.append(dl[0])
        datalist0y.append(dl[1])
    elif resultlist[i]==resultlistset[1]:
        datalist1x.append(dl[0])
        datalist1y.append(dl[1])
    elif resultlist[i]==resultlistset[2]:
        datalist2x.append(dl[0])
        datalist2y.append(dl[1])
    elif resultlist[i]==resultlistset[3]:
        datalist3x.append(dl[0])
        datalist3y.append(dl[1])
    i+=1
axes.scatter( datalist0x,datalist0y, color='red', marker='x', label='0')

axes.scatter(datalist1x,datalist1y, color='blue', marker='o', label='0')

axes.scatter(datalist2x,datalist2y, color='black', marker='.', label='0')

axes.scatter(resultlistx, resultlisty, color='green', marker='*', label='0')

plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper left')
import time
# plt.savefig(str(time.time())+'.png')
plt.show()
