#coding=utf-8
from flask import Flask#rest api web服务 实例
app = Flask(__name__)
@app.route('/doResponse', methods=['GET'])#服务路径 和  appname相同
def scrapy():
    return 'hello,world'
@app.route('/check', methods=['GET'])#健康检查url  
def check():
    return 'success'
class DoResponseApp():
    appname='doResponse'
    def __init__(self,host,port):
        self.host=host
        self.port=port
    def run(self):
        app.run(host=self.host,port=self.port)