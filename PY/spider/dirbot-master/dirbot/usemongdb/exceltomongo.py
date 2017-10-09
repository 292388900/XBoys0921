# encoding:utf=8
import xlrd
import os
import sys
import json
import pymongo
from pymongo import MongoClient
root="F:/bigdata/raw"
excelname="sbi"
suffix=".xlsx"
#连接数据库
client=MongoClient('localhost',27017)
#数据库名
db=client['bigdata']

#'F:/bigdata/raw/sbi.xlsx'
data=xlrd.open_workbook(os.path.join(root,excelname+suffix))

for table in data.sheets():
    account=db[excelname]
    #读取excel第一行数据作为存入mongodb的字段名
    rowstag=table.row_values(0)
    nrows=table.nrows
    #ncols=table.ncols
    #print rows
    returnData={}
    for i in range(1,nrows):
        #将字段名和excel数据存储为字典形式，并转换为json格式
        returnData[i]=json.dumps(dict(zip(rowstag,table.row_values(i))))
        #通过编解码还原数据
        returnData[i]=json.loads(returnData[i])
        #print returnData[i]
        account.insert(returnData[i])
