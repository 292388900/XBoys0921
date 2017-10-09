#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 对某个用户某个项目的某个number的
# issue 及相关的comment和events 进行下载，
# 下载到mongdb 数据库中的 androidbug 数据库中的 [issues,events,comments去]

user = 'dexafree'
repo = 'MaterialList'
number = 74
dbname = 'androidbug'


def getUrl(number='105', type='issues', user='dexafree', repo='MaterialList'):
    # dexafree/MaterialList/issues
    rooturl = 'https://api.github.com/repos/' + user + '/' + repo
    url=rooturl
    if type == 'issues':
        url=rooturl + '/' + 'issues' + '/' + number
    elif type == 'comments':
        url=rooturl + '/' + 'issues' + '/' + number + '/' + 'comments'
    elif type == 'events':
        url= url + '/' + 'issues' + '/' + number + '/' + 'events'
    else:
        return None
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
    except urllib2.HTTPError, e:
        print '<',url,
        print e.code, e.reason,'>',
        return "{}"
    ret = response.read()
    # 获取服务器返回的页面信息
    return ret


from pymongo import MongoClient


def downloaddata(number=number, user=user, repo=repo):
    print 'issue:(', user, ',', repo, ',', number, ')'
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
        elif dict.__class__ == {}.__class__:
            dict['number'] = number
        if len(dict)==0:
            print '<','dict length is zero','>',
        else:
            coll.insert(dict)

    # issues
    print ' .',
    download('issues')
    # comments
    print '.',
    download('comments')
    # events
    print '.',
    download('events')
    print '.'


if __name__ == "__main__":
    downloaddata()
