import  numpy
list=[]
import random
def genRondom():
    result=[]
    x=random.random()*10-5
    y=random.random()*10-5
    result.append((x))
    result.append((y))
    # z=0
    # if x>0:
    #     z=z+1
    # if y>0:
    #     z=z+2
    # result.append((z))
    return result
for i in range(120):
    list.append(genRondom())
name='data'
numpy.savetxt(name+'1.csv',list, delimiter = ',')
