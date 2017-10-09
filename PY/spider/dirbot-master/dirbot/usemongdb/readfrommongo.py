# encoding:utf=8
from pymongo import MongoClient

client = MongoClient()
# admin
# local
# test
for dbname in client.database_names():
    print dbname
# 连接数据库
db = client['bigdata']
# 连接对应的数据集
for collname in db.collection_names():
    print "bigdata:",collname
#collection
coll = db['sbi']
print coll

cursor=coll.find({"企业性质": "有限责任","供应商状态":"正式供应商","注册资金（万元）": {"$lt": 200}})
print cursor.count()

print cursor[0]


import json
from bson import ObjectId

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)

        return json.JSONEncoder.default(self, o)

print JSONEncoder().encode(cursor[0]).decode("unicode_escape")

print  cursor.__class__
print cursor[0].__class__

for obj in cursor:
    print JSONEncoder().encode(obj).decode("unicode_escape")
