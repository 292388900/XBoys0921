import os
import datetime
from string import  Template

tplFilePath = 'F:/website/np/data.temp'
path = 'F:/website/np/data/'

def copy(id=id):
    filename = 'data'+str(id)+'.py'

    tplFile = open(path+filename)
    gFile = open(tplFilePath ,"w")
    #method 1 with Template and substitute(safe_substitute)
    fileList = tplFile.readlines()

    for fileLine in fileList:
        line = fileLine
        gFile.writelines(line)
    tplFile.close()
    gFile.close()
def update(id=id, key='input', value=[0, 0, 0]):
    copy(id=id)

    filename = 'data'+str(id)+'.py'

    tplFile = open(tplFilePath)
    gFile = open(path+filename ,"w")
    #method 1 with Template and substitute(safe_substitute)
    fileList = tplFile.readlines()

    for fileLine in fileList:
        if fileLine.startswith(key):
            line = key+'='+str(value) + '\n'
        else:
            line = fileLine
        gFile.writelines(line)
    tplFile.close()
    gFile.close()
# copy()
# update(key='input',value=[1,2,3])
# update(key='weight',value=[0.4,0.5,0.6])
# update(key='connect',value=[])
def updaterandom(id=id):
    import random
    def r(x=[1,2],y=1,z=False):
        for i in range(len(x)):
            if z:
                x[i]=int(random.random()*y)
            else:
                x[i]=(random.random()*y)
        return x
    input=r(x=[0, 0])
    weight=r(x=[0,0],y=2)
    update(id=id,key='input',value=input)
    update(id=id,key='weight',value=weight)
