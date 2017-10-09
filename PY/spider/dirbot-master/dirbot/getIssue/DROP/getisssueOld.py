# coding=utf8

#避免字符异常
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from github import Github
import networkx as nx
#使用的项目：
#https://github.com/dexafree/MaterialList
#token：26bcc8aeb5ba2c3d090db892acbc3b5fa6c97d26
ACCESS_TOKEN = '26bcc8aeb5ba2c3d090db892acbc3b5fa6c97d26'
USER = 'dexafree'
REPO = 'MaterialList'

client = Github(ACCESS_TOKEN)
user = client.get_user(USER)
repo = user.get_repo(REPO)
#获得所有issues
#使用state=u''，可以获取所有issues
issues=repo.get_issues(state=u'')
# print "issues:",issues
# i=0
# for x in issues:
#     i+=1
#     print i
#     print x
# print i

#使用number获取
issue=repo.get_issue(int(120))
#body
print "issue.body",issue.body
print "issue.coments",issue.comments
print "closed_at",issue.comments
print "title",issue.title
print "state",issue.state
print "labels",issue.get_labels
print "comment_url",issue.comments_url
print "html_url",issue.html_url
print "issue:",issue
#评论
coments=issue.get_comments()
for x in coments:
    print "coment",x

#事件
events=issue.get_events()
for x in events:
    print "event",x
    print "id",x.id
#标签
labels=issue.get_labels()
for x in labels:
    print "label",x


issues_comment=repo.get_issues_comments()

print issues_comment
# for x in issues_comment:
#     print x

# print len(list(repo.get_issues()))

