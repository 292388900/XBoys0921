centos7安装docker

####安装
curl -sSL https://get.docker.com/ | sh
####启动
sudo service docker start
####使用hello-world镜像验证是否安装成功
sudo docker run hello-world


	Unable to find image 'hello-world:latest' locally
	latest: Pulling from library/hello-world
	b04784fba78d: Pull complete 
	Digest: sha256:f3b3b28a45160805bb16542c9531888519430e9e6d6ffc09d72261b0d26ff74f
	Status: Downloaded newer image for hello-world:latest
	
	Hello from Docker!
	This message shows that your installation appears to be working correctly.
	
	To generate this message, Docker took the following steps:
	 1. The Docker client contacted the Docker daemon.
	 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
	 3. The Docker daemon created a new container from that image which runs the
	    executable that produces the output you are currently reading.
	 4. The Docker daemon streamed that output to the Docker client, which sent it
	    to your terminal.
	
	To try something more ambitious, you can run an Ubuntu container with:
	 $ docker run -it ubuntu bash
	
	Share images, automate workflows, and more with a free Docker ID:
	 https://cloud.docker.com/
	
	For more examples and ideas, visit:
	 https://docs.docker.com/engine/userguide/

####查看docker版本
docker version

	Client:
	 Version:      17.06.0-ce
	 API version:  1.30
	 Go version:   go1.8.3
	 Git commit:   02c1d87
	 Built:        Fri Jun 23 21:20:36 2017
	 OS/Arch:      linux/amd64
	
	Server:
	 Version:      17.06.0-ce
	 API version:  1.30 (minimum version 1.12)
	 Go version:   go1.8.3
	 Git commit:   02c1d87
	 Built:        Fri Jun 23 21:21:56 2017
	 OS/Arch:      linux/amd64
	 Experimental: false

