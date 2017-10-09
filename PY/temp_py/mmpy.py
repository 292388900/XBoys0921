
def pp(a):
    print str(a/100)+str(a%100/10)+str(a%10),
def pp0(a):
    print str(a%10),
def pp1(a):
    print str(a%100/10),
def pp2(a):
    print str(a/100),
pp(12)
print
for i in range(11,100):
    for j in range(11,100):
        # print i,"*",j,
        print "",
        if (i*j%10==6):
            pp2(i*j/10)
        else:
            print " ",
    print
x=8
for i in range(11,100):
    for j in range(11,100):
        if i >=j:
            if i*j/1000==x:
                if (i-1)*j/1000==x-1 | (j-1)*i/1000==x-1 :
                   print i,"*",j

for i in range(1,10):
    for j in range(1,10):
        if i*j%10>5:
            pp(i*j)
        else:
            print "   ",
    print
print
for i in range(1,10):
    for j in range(1,10):
        if i*j%10==4:
            pp(i*j)
        else:
            print "   ",
    print
def getS(a):
    t=0
    while(a>0):
        t=a
        a=a/10
    return t
print getS(34)
for  i in range(11,50):
    for j in range(11,50):
        for k in range(1,5):
            for l in range(1,5):
                if i<=j:
                    if i%10<5:
                        if j%10<5:
                            z=(i*10+k)*(j*10+l)
                            if not getS(i*j)==getS(z):
                                print i,j,k,l





