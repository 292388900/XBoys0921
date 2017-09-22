centos 将用户组加入souduers

[root@localhost ~]# chmod u+w /etc/sudoers
[root@localhost ~]# visudo

 xxx ALL=(ALL)  NOPASSWD: ALL

[root@localhost ~]# chmod u-w /etc/sudoers

####方案2 
http://greenzb.blog.51cto.com/745896/1131362

