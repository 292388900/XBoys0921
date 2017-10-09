filename='F:/log/androidbug/dl/download.log'
import time
def ft():
    return time.strftime("%Y%m%d%H%M%S", time.localtime())
import os
import shutil
def creatlog(filename=filename):
    dir=os.path.dirname(filename)
    print dir
    if not os.path.exists(filename):
        print 'file not exist'
        if not os.path.exists(dir):
            print 'dir not exist'
            os.makedirs(dir)
        elif os.path.exists(dir):
            print 'dir exist'
    if not os.path.exists(filename):
        open(filename, 'w').close()
    elif os.path.exists(filename):
        print 'exist'
        filecopy=os.path.join(dir,ft()+".log")
        shutil.copy(filename,filecopy)

if __name__ == "__main__":
    creatlog()

