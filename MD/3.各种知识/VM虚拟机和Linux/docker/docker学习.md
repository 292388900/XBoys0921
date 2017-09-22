Docker学习与安装
http://www.jianshu.com/p/7a58ad7fade4

##原理篇
1.更快交付应用
2.部署和测试更简单
3.实现更高密度和更多的负载

轻量级，可移植

####底层实现  
+ 基础是Linux容器技术
+ 进一步封装
+ 使用Cgroups来提供容器隔离，union文件系统用于保存镜像并使容器变得短暂
	+ Cgroups：linux内核功能
		+ 限制Linux进程组的资源占用（内存和cpu）
		+ 为进程组制作 PID、UTS、IPC、网络、用户及装载命名空间
	+ Union文件系统：文件系统可以被装载在其他文件系统之上

####与虚拟机的区别
共享系统内核，仅包含应用和依赖

####特性

+ 交互式shell
+ 文件系统隔离
+ 写时复制
+ 资源隔离
+ 网络隔离
+ 日志记录
+ 变更管理

####docker结构引擎

![](http://upload-images.jianshu.io/upload_images/670122-9e1e42f04aecefca.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

+ server ：docker守护进程
+ rest api：与server交互和执行命令
+ client：shell,客户书写指令的地方

+ Image：镜像
+ container：容器
+ network：容器暴露端口与主机端口绑定
+ volume：外挂，持久化数据和共享数据

####docker运行流程

![](http://upload-images.jianshu.io/upload_images/670122-58c059c355a0ea48.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

+拉取镜像
+创建容器
+分配文件系统
+分配网络
+设置ip
+运行程序
+捕获并提供应用输出。