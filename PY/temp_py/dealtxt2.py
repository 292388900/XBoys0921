#!/usr/bin/env python
# coding: utf-8
import jieba
file = open("raw3.txt.txt")
jieba.load_userdict("dict.txt")
Group={}
GroupN={}
GroupL={}
while 1:
    lines = file.readlines(100000)
    if not lines:
        break
    for line in lines:

        seg_list =jieba.cut(line, cut_all=False)
        result=[]
        for seg in seg_list:
            result.append(seg)
        i=0
        for g in result:
            if g==u"石神":
                Group[g] = Group.get(g, 0) + 1
                if i-1>=0:
                    GroupL[result[i-1]]=GroupL.get(result[i-1],0)+1
                if i+1<=len(result):
                    GroupN[result[i+1]]=GroupN.get(result[i+1],0)+1
            i+=1
        # seg_list =jieba.cut(line, cut_all=False)
        # for seg in seg_list:
        #     if not g==" ":
        #         print seg,
        # print
        # print("Default Mode: " + "/ ".join(seg_list))  # 精确模式
sortGroup= sorted(Group.items(), key=lambda d: d[1], reverse=True)
print len(sortGroup)
for key in sortGroup:
    print key[0],key[1]
    # print sortGroup.get(key)
sortGroup= sorted(GroupL.items(), key=lambda d: d[1], reverse=True)
print len(sortGroup)
for key in sortGroup:
    print key[0],key[1]
    sortGroup= sorted(GroupN.items(), key=lambda d: d[1], reverse=True)
print len(sortGroup)
for key in sortGroup:
    print key[0],key[1]

