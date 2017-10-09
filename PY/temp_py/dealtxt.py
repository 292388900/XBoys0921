#!/usr/bin/env python
# coding: utf-8
import jieba

jieba.load_userdict("dict.txt")
stopwords = {}.fromkeys([ line.rstrip() for line in open('stopword_all.txt') ])
def getsortGroup():
    file = open("temp.txt")
    Group={}
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
    sortGroup= sorted(Group.items(), key=lambda d: d[1], reverse=True)
    return sortGroup
def getIndex(word=None):
    file = open("temp.txt")
    GT={}
    index=[]
    while 1:
        lines = file.readlines(100000)
        if not lines:
            break
        for line in lines:
            seg_list =jieba.cut(line, cut_all=False)
            result=seg_list
            i=0
            temp=[]
            for g in result:
                if g.encode("utf-8") in stopwords.keys():
                    pass
                elif g.encode("utf-8")==" ":
                    pass
                elif g.encode("utf-8")=="\n":
                    pass
                else:
                    temp.append(g)
            if word in temp:
                for t in temp:
                    GT[t]=GT.get(t,0)+1
                index.append(temp.count(word))
            else:
                index.append(0)
    result=[GT,index]
    return result
def sortPrint(Group=[]):
    sortGroup= sorted(Group.items(), key=lambda d: d[1], reverse=True)
    for key in sortGroup:
        print key[0],key[1]
    return sortGroup
sortGroup=getsortGroup()
# print len(sortGroup)
def judge(index1=[],index2=[]):
    index=[]
    length=len(index1)
    for i in range(length):
        index.append(min(index1[i],index2[i]))

    result=0
    for i in range(length):
        result+=index[i]
    return result

GroupIndex=[]
id=0
for key in sortGroup:
    if key[1]>2:
        print id, key[0],key[1],
        result=getIndex(key[0])
        index=result[1]
        GroupIndex.append((key[0],index))
        print index
        id+=1
import networkx as nx
import matplotlib.pyplot as plt
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
G=nx.Graph()
relation=[]
for line1 in GroupIndex:
    key1=line1[0]
    index1=line1[1]
    list=[]
    for line2 in GroupIndex:
        key2=line2[0]
        index2=line2[1]
        judgresult= judge(index1,index2)
        if judgresult>1:
            G.add_weighted_edges_from([(key1,key2,judgresult)])
        print judgresult,
    print
font = {'family' : 'serif',
        'color'  : 'darkred',
        'weight' : 'normal',
        'size'   : 32,
        }
pos = nx.spring_layout(G)
nx.draw(G, pos=pos, with_labels=True,node_size=900,font_size=20)
plt.show()
for line1 in GroupIndex:
    key1=line1[0]
    index1=line1[1]
    list=[]
    for line2 in GroupIndex:
        key2=line2[0]
        index2=line2[1]
        judgresult= judge(index1,index2)
        list.append(judgresult)
    list.remove(max(list))
    maxvalue=list.index(max(list))
    relation.append((GroupIndex.index(line1),maxvalue))
    print GroupIndex.index(line1),maxvalue

memory=set()
for i in range(len(relation)):
        n=i
        memory=set()
        memory.add(n)
        r=relation[i]
        while True:
            print GroupIndex[r[0]][0],
            n=r[1]
            if n in memory:
                break
            memory.add(n)
            r=relation[n]
        print
    # print "GT"
    # sortPrint(GT)
    # print sortGroup.get(key)
