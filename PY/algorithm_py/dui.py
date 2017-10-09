
def getParent(i):
    return (i-1)/2

def printdui(A):
    for i  in range(0,getParent(len(A)-1)+1):
        if (i+1)*2<len(A):
            print i,":",A[i],A[(i+1)*2-1],A[(i+1)*2],
        else:
            print i,":",A[i],A[(i+1)*2-1],
        print
print getParent(10)

import random
A=[]
for i in range(20):
    A.append(int(random.random()*30)+1)
print A
A=[19, 27, 30, 2, 12, 14, 14, 17, 28, 8, 6, 21, 10, 26, 22, 24, 24, 11, 1, 22,2]
print A

def getlast():
    return getParent(len(A)-1)
def getMaxdui(A,i):
    aisMax=False
    t=getlast()+1
    if i in range(0,t):
        if (i+1)*2<len(A):

            a=A[i]
            b=A[i*2+1]
            c=A[(i+1)*2]

            if a>=b:
                if a>=c:
                    aisMax=True
                else:
                    A[i]=c
                    A[(i+1)*2]=a
                    getMaxdui(A,(i+1)*2)
            else:
                if b>=c:
                    A[i]=b
                    A[i*2+1]=a
                    getMaxdui(A,i*2+1)
                else:
                    A[i]=c
                    A[(i+1)*2]=a
                    getMaxdui(A,(i+1)*2)
        else:
            a=A[i]
            b=A[i*2+1]
            if a<b:
                A[i]=b
                A[i*2+1]=a
            else:
                aisMax=True
def initdui(A):
    t=getlast()+1
    for i  in range(t):
        i=t-1-i
        getMaxdui(A,i)
result=[]

initdui(A)

for i in range(len(A)):
    result.append(A[0])
    A[0]=-100
    getMaxdui(A,0)

print result
printdui(result)



