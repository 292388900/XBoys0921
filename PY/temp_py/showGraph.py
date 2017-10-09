#!/usr/bin/env python
# coding: utf-8
import networkx as nx
import matplotlib.pyplot as plt
from pylab import mpl
import dealtxt0 as d0
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
G=nx.Graph()
relation=d0.relation
GroupIndex=d0.getGrouoIndex(5)
for line in GroupIndex:
    key= line[0]
    G.add_node(key)
for line1 in GroupIndex:
    key1=line1[0]
    index1=line1[1]
    list=[]
    for line2 in GroupIndex:
        key2=line2[0]
        index2=line2[1]
        judgresult= d0.judge(index1,index2)
        if judgresult>1:
            G.add_weighted_edges_from([(key1,key2,judgresult)])
        print judgresult,
    print
pos = nx.spring_layout(G)
ncenter=0
p=nx.single_source_shortest_path_length(G,ncenter)
plt.figure(figsize=(8,8))
nx.draw_networkx_edges(G,pos,nodelist=[ncenter],alpha=0.4)
nx.draw_networkx_nodes(G,pos,nodelist=p.keys(),
                       node_size=80,
                       node_color=p.values(),
                       cmap=plt.cm.Reds_r)
plt.axis('off')
plt.savefig("weighted_graph.png") # save as png
plt.show() # display


# nx.draw(G, pos=pos,node_color="r", with_labels=True,node_size=900,font_size=14)
# plt.show()
