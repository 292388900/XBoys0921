#!/usr/bin/env python
# coding: utf-8
import jieba

jieba.load_userdict("dict.txt")
stopwords = {}.fromkeys([ line.rstrip() for line in open('stopword_all.txt') ])
Group={}
def getGroup():
    file = open("temp.txt")
    while 1:
        lines = file.readlines(100000)
        if not lines:
            break
        for line in lines:
            seg_list =jieba.cut(line, cut_all=False)
            result=seg_list
            i=0
            for g in result:
                if g.encode("utf-8") in stopwords.keys():
                    pass
                elif g.encode("utf-8")==" ":
                    pass
                elif g.encode("utf-8")=="\n":
                    pass
                else:
                    print g,
                    Group[g] = Group.get(g, 0) + 1
            print
    return Group
Group=getGroup()

def getlinenum():
    linenum=0
    file = open("temp.txt")
    while 1:
        lines = file.readlines(100000)
        if not lines:
            break
        for line in lines:
            linenum+=1
    return linenum
linenum= getlinenum()
indexGroup={}
def initIndexGroup():
    for key in Group.keys():
        list=[]
        for i in range(linenum):
            list.append(0)
        indexGroup[key]=list
    return indexGroup
indexGroup=initIndexGroup()

# for key in indexGroup:
#     print key ,
#     print indexGroup[key]


def getIndexGroup():
    file = open("temp.txt")
    lineid=-1
    while 1:

        lines = file.readlines(100000)
        if not lines:
            break
        for line in lines:
            lineid += 1
            seg_list = jieba.cut(line, cut_all=False)
            result = seg_list
            i = 0
            temp = []
            for g in result:
                if g.encode("utf-8") in stopwords.keys():
                    pass
                elif g.encode("utf-8") == " ":
                    pass
                elif g.encode("utf-8") == "\n":
                    pass
                else:
                    temp.append(g)
            for word in temp:
                indexGroup.get(word)[lineid]=temp.count(word)
getIndexGroup()
sortGroup= sorted(Group.items(), key=lambda d: d[1], reverse=True)
GroupIndex=[]

def judge(index1=[],index2=[]):
    index=[]
    length=len(index1)
    for i in range(length):
        index.append(min(index1[i],index2[i]))
    result=0
    for i in range(length):
        result+=index[i]
    return result
print len(sortGroup)
def getGrouoIndex(size=2):
    for key in sortGroup:
        id = sortGroup.index(key)
        if key[1]>size:
            print id, key[0],key[1],
            index=indexGroup.get(key[0])
            GroupIndex.append((key[0],index))
            print
            # print index
    return  GroupIndex
def getRelation(size=2):
    GroupIndex = getGrouoIndex(size)
    relation=[]
    for line1 in GroupIndex:
        index1=line1[1]
        list=[]
        for line2 in GroupIndex:
            index2=line2[1]
            judgresult= judge(index1,index2)
            list.append(judgresult)
        relation.append(list)
    return relation
relation=getRelation(20)

for line in relation:
    for r in line:
        print r,
    print


# for key in indexGroup:
#     print key ,
#     print indexGroup[key]

