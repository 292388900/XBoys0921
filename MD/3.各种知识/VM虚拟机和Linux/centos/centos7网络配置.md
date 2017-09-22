centos 7 网络配置
http://www.imooc.com/article/16648
nmtui

设置默认开启网卡

http://jingyan.baidu.com/article/7f766daf992cd14101e1d028.html

1
进入终端
cd /etc/sysconfig/network-scripts
2
vi打开对应网卡配置文件，centos默认网卡为ens33，其它系统大多为enth0
vi ifcfg-ens33
3
将ONBOOT=no改为ONBOOT=yes
wq保存

vmware 三种网络配置的区别
桥接：如同主机
nat：nat路由器
只主机：只和主机通信