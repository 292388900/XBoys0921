# coding=utf8
from uselog import dl
# 避免字符异常
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

from github import Github

# 使用的项目：
# https://github.com/dexafree/MaterialList
# token：26bcc8aeb5ba2c3d090db892acbc3b5fa6c97d26
ACCESS_TOKEN = '26bcc8aeb5ba2c3d090db892acbc3b5fa6c97d26'
USER = 'dexafree'
REPO = 'MaterialList'

client = Github(ACCESS_TOKEN)
user = client.get_user(USER)
repo = user.get_repo(REPO)
# 获得所有issues
# 使用state=u''，可以获取所有issues
issues = repo.get_issues(state=u'')


def getsize(issues):
    size = 1;
    for issue in issues:
        size += 1
    return size

import downloadURN
import time

def ft(time):
    t = int(time)
    info= str(t % 86400 / 3600)+ ' '+ str(t % 3600 / 60)+' '+ str(t % 60)+' '+str(time - t)
    dl.debug('time:'+info)
def getissues(user=USER,repo=REPO):
    stime = time.time()
    # 从1开始
    for i in range(1, getsize(issues)+1):
        tstime = time.time()
        downloadURN.downloaddata(user=user, repo=repo, number=i)
        tetime = time.time()
        ft(tetime - tstime)
    etime = time.time()
    ft(etime - stime)
if __name__ == "__main__":
    getissues()
    # dropdb('androidbug')
