#!/usr/bin/env python
# coding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
#
#将bat文件分解成 temp.txt文件
#
#
def srawtotemp(filename="test.dat"):
    file = open(filename)
    import jieba
    i=0;
    j=0;
    oldj=-1;
    fdes = open('temp/temp'+str(j)+'.txt', 'w')
    while 1:
        i+=1
        j=i/33
        if oldj==j:
            pass
        else:
            fdes.close()
            fdes = open('temp/temp'+str(j)+'.txt', 'w')
            oldj=j
        lines = file.readlines(100000)
        if not lines:
            break

        for line in lines:
            seg_list =jieba.cut(line, cut_all=False)
            result=seg_list
            s=''
            for g in result:
                if g.encode("utf-8")==" ":
                    pass
                elif g.encode("utf-8")=="\t":
                    pass
                elif g.encode(("utf-8"))=="　":
                    pass
                elif g.encode("utf-8")=="\n":
                    pass
                elif g.encode("utf-8")=="。":
                    print s+"。"
                    fdes.write(s+"。\n")
                    s=""
                else:
                    s+=g+""
        fdes.flush()
srawtotemp()
