#!/usr/bin/env python
# coding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

#文件内容格式化，存放到temp.txt文件中

def srawtotemp(filename="raw.txt"):
    file = open(filename)
    fdes = open('temp.txt', 'w')
    import jieba
    while 1:
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
    fdes.close()
srawtotemp()
