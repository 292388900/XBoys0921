#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 对某个用户某个项目的某个number的
# issue 及相关的comment和events 进行下载，
# 下载到mongdb 数据库中的 androidbug 数据库中的 [issues,events,comments去]
from uselog import dl

USER = 'dexafree'
REPO = 'MaterialList'
number = 74
dbname = 'androidbug'


def getUrl(number='105', type='issues', user=USER, repo=REPO):
    # dexafree/MaterialList/issues
    rooturl = 'https://api.github.com/repos/' + user + '/' + repo
    url=rooturl
    if type == 'issues':
        url= rooturl + '/' + 'issues' + '/' + number
    elif type == 'comments':
        url= rooturl + '/' + 'issues' + '/' + number + '/' + 'comments'
    elif type == 'events':
        url= rooturl + '/' + 'issues' + '/' + number + '/' + 'events'
    else:
        url=None
    return url


import urllib2
import json


def http_get(url):
    headers = \
        {
            'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',
            'Authorization': 'token 26bcc8aeb5ba2c3d090db892acbc3b5fa6c97d26'
        }
    try:
        # 页面的地址
        req = urllib2.Request(url=url, headers=headers)
        # 调用urllib2向服务器发送get请求
        response = urllib2.urlopen(req)
    except urllib2.URLError, e:
        info=url, str(e.code),e.reason
        dl.debug(info)
        return "{}"
    ret = response.read()
    # 获取服务器返回的页面信息
    return ret


from pymongo import MongoClient

def downloaddata(number=number, user=USER, repo=REPO):
    tup=user, repo, number
    info= 'issue:'+ str(tup)
    dl.debug(info)
    # 连接数据库
    client = MongoClient('localhost', 27017)

    # 数据库名
    def download(type):
        # dbname='androidbug'
        db = client[dbname]
        coll = db[type]
        url = getUrl(type=type, number=str(number), user=user, repo=repo)
        ret = http_get(url)
        dict = json.loads(ret)
        # print  json.dumps(dict,sort_keys=True,indent=4)
        # add number 属性
        if dict.__class__ == [].__class__:
            for d in dict:
                d['number'] = number
                d['user']=user
                d['repo']=repo
        elif dict.__class__ == {}.__class__:
            dict['number'] = number
            dict['user']=user
            dict['repo']=repo

        if len(dict)==0:
            info= '<dict length is zero>',
            dl.debug(info)
        else:
            coll.insert(dict)

    # issues
    dl.debug(' .')
    download('issues')
    # comments
    dl.debug(' .')
    download('comments')
    # events
    dl.debug(' .')
    download('events')
    dl.debug(' .')


if __name__ == "__main__":
    downloaddata()
