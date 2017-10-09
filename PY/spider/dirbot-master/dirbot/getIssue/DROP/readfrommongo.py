# encoding:utf=8
import json
from bson import ObjectId

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


from pymongo import MongoClient

client = MongoClient()
db = client['androidbug']
coll = db['issues']

cursor=coll.find({'number':105})
print cursor.count()
for obj in cursor:
    print obj['number']
    # print JSONEncoder().encode(obj).decode("unicode_escape")

coll = db['events']
cursor=coll.find({"number":105})
print cursor.count()
for obj in cursor:
    print JSONEncoder().encode(obj).decode("unicode_escape")
