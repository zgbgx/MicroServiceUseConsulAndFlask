# MicroServiceUseConsulAndFlask
use consul and flask to build a microservice demo(用consul作为服务注册和发现的中心，使用flask作为http服务器开发的微服务demo）

# 项目所用到的package
consulate flask request,均可用 pip 安装<br>
# 关于客户端和服务端
分别运行 server和server2 在不同端口启动两个doResponse服务端<br>
每启动一个服务，调用 consulate.Consul.agent.service.register方法，注册一个服务，同事在http 服务上实现'/check' 这个接口，提供给consul做健康监测.<br>
运营client 会请求consul 得到可用的 服务 主机和端口，随机请求一个可用的服务地址。
# 关于consul
使用consul作为服务注册和发现及健康监测中心<br>
![image](https://github.com/zgbgx/MicroServiceUseConsulAndFlask/blob/master/service.png)<br>
你可以在  https://www.consul.io/downloads.html 下载系统对应的 consul版本，下载后解压缩 得到一个可执行文件  可用./consul agent -dev 已默认配置启动consul(默认的consul api 及 web 客户端 端口是 8500).<br>
更多关于 consul ，你可以浏览 https://www.consul.io/
