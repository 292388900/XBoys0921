import os
rootdir="F:/website/"
sitename='test'
subdirs=\
[
    "templates",
    "static",
    "static/js",
    "static/css"
]
for subdir in subdirs:
    dir=os.path.join(rootdir,sitename,subdir)
    if not os.path.exists(dir):
        os.makedirs(dir)

