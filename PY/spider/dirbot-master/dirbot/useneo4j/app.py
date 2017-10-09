# coding=utf-8
from flask import Flask, jsonify, render_template
from py2neo import Graph

app = Flask(__name__)
graph = Graph()

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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/graph')
def get_graph():
    nodes = map(buildNodes, graph.run('MATCH (n) RETURN n'))
    edges = map(buildEdges, graph.run('MATCH ()-[r]->() RETURN r'))

    return jsonify(elements = {"nodes": nodes, "edges": edges})

if __name__ == '__main__':
    app.run(debug = True)
