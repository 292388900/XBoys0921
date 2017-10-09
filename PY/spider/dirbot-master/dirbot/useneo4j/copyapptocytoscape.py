# -*- coding: cp936 -*-
import sys,os

import makecytoscapedir
#获得当前脚本的路径
def cur_file_dir():
     path = sys.argv[0]
     if os.path.isdir(path):
         return path
     elif os.path.isfile(path):
         return os.path.dirname(path)
#创建目录和文件
path=cur_file_dir()
import shutil
appdir=makecytoscapedir.rootdir

if not os.path.exists(appdir):
    print "dir not exist"
shutil.copy(os.path.join(path,'app.py'), appdir)
desfile=os.path.join(appdir, 'app.py')
print 'desfile:'+desfile

