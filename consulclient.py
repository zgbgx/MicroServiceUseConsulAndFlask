#coding=utf-8
from consulate import Consul
from random import randint
import requests
import json
#consul 操作类
class ConsulClient():
    def __init__(self,host=None,port=None,token=None):#初始化，指定consul主机，端口，和token
        self.host=host#consul 主机
        self.port=port#consul 端口
        self.token=token
        self.consul=Consul(host=host,port=port)
    def register(self,name,service_id,address,port,tags,interval,httpcheck):#注册服务 注册服务的服务名  端口  以及 健康监测端口
        self.consul.agent.service.register(name,service_id=service_id,address=address,port=port,tags=tags,interval=interval,httpcheck=httpcheck)
    def getService(self,name):#负债均衡获取服务实例
        url='http://'+self.host+':'+str(self.port)+'/v1/catalog/service/'+name#获取 相应服务下的DataCenter
        dataCenterResp=requests.get(url)
        if dataCenterResp.status_code!=200:
            raise Exception('can not connect to consul ')
        listData=json.loads(dataCenterResp.text)
        dcset=set()#DataCenter 集合 初始化
        for service in listData:
            dcset.add(service.get('Datacenter'))
        serviceList=[]#服务列表 初始化
        for dc in dcset:
            if self.token:
                url='http://'+self.host+':'+self.port+'/v1/health/service/'+name+'?dc='+dc+'&token='+self.token
            else:
                url='http://'+self.host+':'+self.port+'/v1/health/service/'+name+'?dc='+dc+'&token='
            resp=requests.get(url)
            if resp.status_code!=200:
                raise Exception('can not connect to consul ')
            text=resp.text
            serviceListData=json.loads(text)
            
            for serv in serviceListData:
                status=serv.get('Checks')[1].get('Status')
                if status=='passing':#选取成功的节点
                    address=serv.get('Service').get('Address')
                    port=serv.get('Service').get('Port')
                    serviceList.append({'port':port,'address':address})
        if len(serviceList)==0:
            raise Exception('no serveice can be used')
        else:
            service=serviceList[randint(0,len(serviceList)-1)]#随机获取一个可用的服务实例
            return service['address'],int(service['port'])