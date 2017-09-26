#coding=utf-8
from consulclient import ConsulClient
from httpapp import DoResponseApp
class HttpServer():
    #新建服务时，需要指定consul服务的 主机，端口，所启动的 服务的 主机 端口 以及 restful http 服务 类
    def __init__(self,host,port,appname,consulhost,consulport,appClass):
        self.port=port
        self.host=host
        self.appname=appname
        self.consulhost=consulhost
        self.consulport=consulport
        self.app=appClass(host=host,port=port)
    def startServer(self):
        client=ConsulClient(host=self.consulhost,port=self.consulport)
        client.register(self.appname,service_id=self.appname+self.host+':'+str(self.port),address=self.host,port=self.port,tags=['master'],
                        interval='30s',httpcheck='http://'+self.host+':'+str(self.port)+'/check')#注册服务 
        self.app.run()#启动服务
if __name__=='__main__':
    server=HttpServer('127.0.0.1',8000,DoResponseApp.appname,'127.0.0.1',8500,DoResponseApp)
    server.startServer()