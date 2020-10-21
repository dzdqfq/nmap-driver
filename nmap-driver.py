import time
import grpc
import nmap
from concurrent import futures
from ipdb import set_trace
import ipam_pb2,ipam_pb2_grpc # 刚刚生产的两个文件

class NmapService(ipam_pb2_grpc.NmapServiceServicer):
    def ipScan(self,request,ctx):
        print('fangwen')
        res=nmapSearch(request.ip)
        #set_trace()	
        return res

def nmapSearch(network_prefix):
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
   	    
def main():
    # 多线程服务器
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # 实例化 计算len的类
    servicer = NmapService()
    # 注册本地服务,方法ComputeServicer只有这个是变的
    ipam_pb2_grpc.add_NmapServiceServicer_to_server(servicer, server)
    # 监听端口
    server.add_insecure_port('[::]:19999')
    # 开始接收请求进行服务
    server.start()
    # 使用 ctrl+c 可以退出服务
    try:
        print("running...")
        time.sleep(1000)
    except KeyboardInterrupt:
        print("stopping...")
        server.stop(0)


if __name__ == '__main__':
    main()


