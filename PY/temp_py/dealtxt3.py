#!/usr/bin/env python
# coding: utf-8
import jieba
file = open("raw2.txt")
jieba.load_userdict("dict.txt")
stopwords = {}.fromkeys([ line.rstrip() for line in open('stopword.txt') ])
Group={}
def initGroup():
    while 1:
        lines = file.readlines(100000)
        if not lines:
            break
        for line in lines:
            seg_list =jieba.cut(line, cut_all=False)
            result=seg_list
            for g in result:
                if g.encode("utf-8") in stopwords.keys():
                    pass
                elif g.encode("utf-8")==" ":
                    pass
                elif g.encode("utf-8")=="\n":
                    pass
                else:
                    Group[g] = Group.get(g, 0) + 1

sortGroup= sorted(Group.items(), key=lambda d: d[1], reverse=True)
print len(sortGroup)
for key in sortGroup:
    print key[0],key[1]
    # print sortGroup.get(key)
