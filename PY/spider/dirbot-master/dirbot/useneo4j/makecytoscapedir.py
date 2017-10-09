import os
rootdir="F:/neo4j/cytoscape/"
subdirs=\
[
    "templates",
    "static",
    "static/js",
    "static/css"
]
for subdir in subdirs:
    dir=os.path.join(rootdir,subdir)
    if not os.path.exists(dir):
        os.makedirs(dir)
    # else:
    #     print "dir already exits"

