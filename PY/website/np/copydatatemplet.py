import os
import datetime
from string import  Template

tplFilePath = 'data.templet'
path = 'data/'
import random
def r(x=[1,2],y=1,z=False):
    for i in range(len(x)):
        if z:
            x[i]=int(random.random()*y)
        else:
            x[i]=(random.random()*y)
    return x

def scon(id=2,x=[1,1]):
    for i in range(2):
        x[i]=(id/2+1)*2+i
    return x

for id in range(12):
    input=r(x=[0, 0])
    weight=r(x=[0,0],y=2)
    connect=scon(id,x=[0,0] )

    filename = 'data'+str(id)+'.py'


    tplFile = open(tplFilePath)
    gFile = open(path+filename ,"w")

    #method 1 with Template and substitute(safe_substitute)
    lines=[]
    tmp=Template(tplFile.read())

    lines.append(tmp.substitute(
                 input = input,
                 weight = weight,
                 id = id,
                 connect = connect,
                 ))
    gFile.writelines(lines)
    tplFile.close()
    gFile.close()
