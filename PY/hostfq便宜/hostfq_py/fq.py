import os
import sys
def getpath():
    if os.path.isfile(sys.argv[0]):
        return os.path.dirname(sys.argv[0])
    elif os.path.isdir(sys.argv[0]):
        return sys.argv[0]
def fqNo():
    os.system(os.path.join(getpath(),"recover.bat"))
    os.system("ipconfig /flushdns")
def fqYes():
    os.system(os.path.join(getpath(), "revise.bat"))
    os.system("ipconfig /flushdns")
def openHost():
    os.system(os.path.join(getpath(), "openhost.bat"))
    os.system("openhost.bat")

if __name__=="__main__":
    fqYes()