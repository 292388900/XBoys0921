#技能+github 操作

打开 git shell

配置用户名和密码
 git config --global user.name "supermans1201"
 git config --global user.email "supermans1201@gmail.com"

创建密钥
 ssh-keygen -t rsa -C "supermans1201@gmail.com"

密钥位置
F:\LM\github_rsa

测试 
ssh -T git@github.com


github设置公
电脑端添加 ssh 私钥

	F:\Users\Super\Documents\GitHub> ssh-add F:/LM/github_rsa/id_rsa
	Enter passphrase for F:/LM/github_rsa/id_rsa:
	Identity added: F:/LM/github_rsa/id_rsa (F:/LM/github_rsa/id_rsa)


其中
.git/config 文件

	[core]
		repositoryformatversion = 0
		filemode = false
		bare = false
		logallrefupdates = true
		symlinks = false
		ignorecase = true
	[remote "origin"]
		url = git@github.com:Supermans1201/XBoys0921.git
		fetch = +refs/heads/*:refs/remotes/origin/*
	[branch "master"]
		remote = origin
		merge = refs/heads/master

合并：

	 git pull origin master

推送：

	 git push origin master

查看分支
	
	git branch

查看修改

	git diff
