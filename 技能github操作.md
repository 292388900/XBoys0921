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

