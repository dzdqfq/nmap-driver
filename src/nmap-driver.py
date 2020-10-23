#!/usr/bin/env python
#-*- coding: UTF-8 -*-
import time
import grpc
import nmap
import configparser
import os
from concurrent import futures
from ipdb import set_trace
import ipam_pb2,ipam_pb2_grpc 
import logging.config

root_dir =os.path.dirname(os.path.dirname(os.path.abspath(__file__)))#获取上一级目录
logging.config.fileConfig(root_dir+"/config"+"/logging.conf")
logger = logging.getLogger('root')

class NmapService(ipam_pb2_grpc.NmapServiceServicer):
    def ipScan(self,request,ctx):
        logger.info('execute nmap scan ip = %s' % request.ip)
        res=nmapSearch(request.ip)	
        return res

def nmapSearch(network_prefix):
    try:
        nm = nmap.PortScanner()
        # 配置nmap扫描参数
        scan_raw_result = nm.scan(hosts=network_prefix, arguments='-sS -O')
        nu=scan_raw_result['nmap']['scanstats']
        ipResponse = ipam_pb2.IpResponse(up=nu['uphosts'],down=nu['downhosts'],total=nu['totalhosts'])
        for host, detail in scan_raw_result['scan'].items():
            if detail['status']['state'] == 'up':
                iplist=ipResponse.result.add()
                iplist.ip=host
                iplist.status='up'
                iplist.os=detail['osmatch'][0]['name']
        return ipResponse
    except Exception as e:
        logger.error('scan %s error: %s' % (network_prefix,e))
        raise e
   	    
def main():
    # 多线程服务器
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # 实例化 计算len的类
    servicer = NmapService()
    # 注册本地服务,方法ComputeServicer只有这个是变的
    ipam_pb2_grpc.add_NmapServiceServicer_to_server(servicer, server)
    # 监听端口
    port = getPort()
    server.add_insecure_port('[::]:'+port)
    # 开始接收请求进行服务
    server.start()
    logger.info('nmap-driver server start port = %s' % port)
    server.wait_for_termination()
    logger.info('nmap-driver server stop port = $s' % port)

def getPort():
    cf = configparser.ConfigParser()
    cf.read(root_dir+"/config"+"/config.ini") 
    port = cf.get("Nmap-Driver", "port")
    return port


if __name__ == '__main__':
    main()


