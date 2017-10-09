# coding=utf8
from github import Github
import networkx as nx

ACCESS_TOKEN = '26bcc8aeb5ba2c3d090db892acbc3b5fa6c97d26'
USER='minrk'
REPO='findspark'
client = Github(ACCESS_TOKEN)
user = client.get_user(USER)
repo=user.get_repo(REPO)
stargazers=list(repo.get_stargazers())#加星的用户集合

print  repo
g = nx.DiGraph()
g.add_node(repo.name + '(repo)', type='repo', lang=repo.language, owner=user.login)

for sg in stargazers:
    g.add_node(sg.login + '(user)', type='user')
    g.add_edge(sg.login + '(user)', repo.name + '(repo)', type='gazes')
# 打印图的基本属性
print (nx.info(g),'\n')
# 打印项目和用户点的基本属性
print (g.node['findspark(repo)'])
print (g.node['luzhijun(user)'],'\n')
# 打印这条边属性
print (g['luzhijun(user)']['findspark(repo)'])
# 打印起点为XXX的信息
print (g['luzhijun(user)'])
print (g['findspark(repo)'])
# 打印用户的出入度信息
print (g.in_edges(['luzhijun(user)']))
print (g.out_edges(['luzhijun(user)']))
# 打印项目的出入度信息
print (g.in_edges(['findspark(repo)']))
print (g.out_edges(['findspark(repo)']))
