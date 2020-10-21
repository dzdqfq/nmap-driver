# nmap-driver服务使用
1.下载nmap:yum install nmap

2.下载nmap-python模块:pip3 install python-nmap

3.下载grpcio模块:pip3 install grpcio

4.下载protobuf模块:pip3 install protobuf

5.下载grpcio_tools模块:pip3 install grpcio_tools

6.下载ipdb模块:pip3 install ipdb

7.启动项目:python3 nmap-driver.py

# docker镜像直接开启nmap-driver服务
1.docker load -i nmap-driver.tar

2.docker run -d -p 19999:19999 --name 容器名字 nmap-driver
