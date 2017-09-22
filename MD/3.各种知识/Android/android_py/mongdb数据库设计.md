##简单的想法
####Mongodb的组织结构
+ client = MongoClient()  
+ 客户端。一个客户端client对应着多个数据库db。
+ db  = client[':user_:repo']
+ 数据库。一个数据库db对应着用户(:user)的一个Android项目(:repo)。
+ coll = db['issues'|'comments'|'commits']
+ 集合。现在包含四个集合。主要的issues，是讨论问题的主要内容。commits，是提交的代码。推测前者和变异算子的描述可能相关；而后者和变异算子的变异相关。
####对于一个Android 项目建立一个db以及4个coll

