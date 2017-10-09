# -*- coding: cp936 -*-
print u'hello world1！'
import sys,os
#获得当前脚本的路径
def cur_file_dir():
     path = sys.argv[0]
     print sys.argv[0]

     if os.path.isdir(path):
         print 'a'
         return path
     elif os.path.isfile(path):
         print 'b:'+os.path.dirname(path)
         return os.path.dirname(path)
#创建目录和文件
path=cur_file_dir()
import shutil
noveldir=os.path.join(path,'novel')
print u'创建目录：'+noveldir
if os.path.exists(noveldir):
    shutil.rmtree(noveldir)
os.mkdir(noveldir)

shutil.copy(os.path.join(path,'novel.py'),noveldir)
desfile=os.path.join(noveldir,'novel.py')
print 'desfile'+desfile
sys.argv[0]=desfile
print '='+sys.argv[0]
import random,time
def runnovel():
    a=random.uniform(10, 20)
    print a
    if a>16:
        execfile(desfile)
runnovel()


