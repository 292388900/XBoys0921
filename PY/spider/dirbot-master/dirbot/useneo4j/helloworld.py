# coding=utf-8
from py2neo import  Node,Relationship
#节点和关系
a = Node("Person",name="Alice")
b=Node("Person",name="Bob")
ab=Relationship(a,"KNOWS",b)
print a
print a.fromkeys('Person')
print a.properties
print b
print ab.type
print ab.start_node()
print ab.end_node()
thenode=set([])
def buildNodes(node):
    data = {"id": str(node[0].properties), "label": next(iter(node[0].labels()))}
    # print node[0]
    thenode.add(str(node[0].properties))

    print "label",next(iter(node[0].labels()))
    return {"data": data}
startnode=set([])
endnode=set([])
def buildEdges(relation):
    data = {"source": str(relation[0].start_node().properties),
            "target": str(relation[0].end_node().properties),
            "relationship": relation[0].type()}
    startnode.add(str(relation[0].start_node().properties))
    endnode.add(str(relation[0].end_node().properties))
    return {"data": data}

from py2neo import Graph
graph=Graph()

g=Graph()
#匹配到所有的node
nodes =g.run("MATCH(n) RETURN n")
#匹配到所有的relationship
edges =g.run("MATCH ()-[r]->() RETURN r")
# for d in nodes:
#     print d[0]
# for d in edges:
#     print d[0]
nodes = map(buildNodes, graph.run('MATCH (n) RETURN n'))
edges = map(buildEdges, graph.run('MATCH ()-[r]->() RETURN r'))

print "1",startnode
print endnode
print thenode
print "3",startnode&endnode
print thenode-(startnode|endnode)
print (startnode|endnode)-thenode
print thenode==(startnode|endnode)
print "5",(thenode|startnode|endnode)-thenode
# print edges.__class__
# for d in edges:
#     print d.keys()
#     set2=d['data']
#     print set2
#
# g=Graph()
# #匹配到所有的node
# nodes =g.run("MATCH(n) RETURN n")
# #匹配到所有的relationship
# edges =g.run("MATCH ()-[r]->() RETURN r")
# for d in nodes:
#     print d[0]
# for d in edges:
#     print d[0]


