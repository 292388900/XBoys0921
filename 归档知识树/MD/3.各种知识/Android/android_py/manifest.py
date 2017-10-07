from xml.etree.ElementTree import parse
import xml.etree.ElementTree as ET
def getElementTree(filePath):
    with open(filePath) as f:
        doc = parse(f)
    return doc
doc=getElementTree("F:/LM/ABA/gnucash-android-master/app/src/main/AndroidManifest.xml")
print doc
def getCount(doc,tag='activity'):
    count = 0
    for elem in doc.iter(tag=tag):
        # print elem.attrib
        count += 1
    print count

getCount(doc,"activity")
getCount(doc,"service")
getCount(doc,"receiver")
getCount(doc,"permission")