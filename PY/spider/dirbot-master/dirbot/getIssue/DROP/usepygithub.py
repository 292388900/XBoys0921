# coding=utf8
from github import Github
import networkx as nx

#token
ACCESS_TOKEN = '26bcc8aeb5ba2c3d090db892acbc3b5fa6c97d26'
USER = 'supermans1201'

#建立连接
client = Github(ACCESS_TOKEN)
user = client.get_user(USER)

# #仓库
REPOS=user.get_repos()
for repo in REPOS:
    print repo.name
USER='minrk'
REPO='findspark'
user = client.get_user(USER)
repo=user.get_repo(REPO)
stargazers=list(repo.get_stargazers())#加星的用户集合
print len(list(repo.get_issues()))
print len(stargazers)
g = nx.DiGraph()
g.add_node(repo.name + '(repo)', type='repo', lang=repo.language, owner=user.login)
#
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

from operator import itemgetter
kkg = nx.generators.small.krackhardt_kite_graph()
print ("Degree Centrality")
print (sorted(nx.degree_centrality(kkg).items(),
             key=itemgetter(1), reverse=True),'\n')
print ("Betweenness Centrality")
print (sorted(nx.betweenness_centrality(kkg).items(),
             key=itemgetter(1), reverse=True),'\n')
print ("Closeness Centrality")
print (sorted(nx.closeness_centrality(kkg).items(),
             key=itemgetter(1), reverse=True))
import sys
for i, sg in enumerate(stargazers):
    # 增加关注联系，如果有关注者的话
    try:
        for follower in sg.get_followers():
            if follower.login + '(user)' in g:
                g.add_edge(follower.login + '(user)', sg.login + '(user)',
                           type='follows')
    except Exception: #ssl.SSLError
        sys.stderr.write( "Encountered an error fetching followers for", \
                             sg.login, "Skipping.")

    print ("Processed", i+1, " stargazers. Num nodes/edges in graph", \
          g.number_of_nodes(), "/", g.number_of_edges())
    print ("Rate limit remaining", client.rate_limiting)
