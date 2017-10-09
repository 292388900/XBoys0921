import os
import datetime
from string import  Template

tplFilePath = 'cell.templet'
path = 'cell/'
for id in range(12):

    filename = 'cell'+str(id)+'.py'
    tplFile = open(tplFilePath)
    gFile = open(path+filename ,"w")

    #method 1 with Template and substitute(safe_substitute)
    lines=[]
    tmp=Template(tplFile.read())

    lines.append(tmp.substitute(
                 id = id,
                 ))
    gFile.writelines(lines)
    tplFile.close()
    gFile.close()
