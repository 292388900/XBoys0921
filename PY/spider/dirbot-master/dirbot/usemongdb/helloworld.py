# encoding:utf=8
from pymongo import MongoClient

client = MongoClient()
print client

# admin
# local
# test
for dbname in client.database_names():
    print dbname
# 连接数据库
db = client['test']
print db
# 连接对应的数据集
for collname in db.collection_names():
    print collname
coll = db['dataset1']
print coll
from datetime import datetime

document = {
    "address": {
        "street": "2 Avenue",
        "zipcode": "10075",
        "building": "1480",
        "coord": [-73.9557413, 40.7720266]
    },
    "borough": "Manhattan",
    "cuisine": "Italian",
    "grades": [
        {
            "date": datetime.strptime("2014-10-01", "%Y-%m-%d"),
            "grade": "A",
            "score": 11
        },
        {
            "date": datetime.strptime("2014-01-16", "%Y-%m-%d"),
            "grade": "B",
            "score": 17
        }
    ],
    "name": "Vella",
    "restaurant_id": "41704620"
}
coll.insert_one(document)

cursor=coll.find()
print cursor
for c in cursor:
    print c

#数据集清空
# coll.drop()
