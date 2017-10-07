#技能+github 操作

打开 git shell

配置用户名和密码
 git config --global user.name ""
 git config --global user.email ""

创建密钥
 ssh-keygen -t rsa -C ""

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

设置文件名中文

	git config core.quotepath false


操作流程

	git diff
	git add .
	git commit -m "修改内容信息"
	git pull origin master
	git push origin master

创建仓库
	
	token:dece69b8e141007bdd8c3b664e79515eaf69c29e

示例

	Invoke-WebRequest  https://api.github.com/user/repos?access_token=dece69b8e141007bdd8c3b664e79515eaf69c29e -Method POST -Body '{"name":"learn-nodejs"}'

添加远程配置：

	 git remote add origin git@github.com:supermans1201/learn-nodejs.git
