centos 远程桌面连接
yum install -y tigervnc-server

####方案1

http://www.jianshu.com/p/35640fc5672b
可行
会遇到一个异常，但没什么影响


启动指令
	
	systemctl start vncserver@:1.service
	systemctl enable vncserver@:1.service
	\rm -R /tmp/.X11-unix/
	systemctl enable vncserver@:1.service
	vncserver
