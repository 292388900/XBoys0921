# encoding:utf=8
from pymongo import MongoClient


# admin
# local
# test
def dropdb(name):
    client = MongoClient()
    print '[client]:', client
    print '---------------------------------'
    for dbname in client.database_names():
        print ':', dbname
        db = client[dbname]
        for collname in db.collection_names():
            print '\t-', collname

            if dbname == name:
                print '\t:drop'
                db[collname].drop()


def printdb():
    client = MongoClient()
    print '[client]:', client
    print '---------------------------------'
    for dbname in client.database_names():
        print ':', dbname
        db = client[dbname]
        for collname in db.collection_names():
            print '\t-', collname
            coll = db[collname]
            print '\tcount:', coll.count()


def readdb(dbname='androidbug', collname='issues'):
    client = MongoClient()
    db = client[dbname]
    coll = db[collname]

    cursor = coll.find()
    print cursor.count()
    for obj in cursor:
        print obj


if __name__ == "__main__":
    printdb()
    readdb()
    # dropdb('androidbug')
