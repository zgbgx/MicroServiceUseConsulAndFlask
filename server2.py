from server import HttpServer
from httpapp import DoResponseApp
server=HttpServer('127.0.0.1',8001,DoResponseApp.appname,'127.0.0.1',8500,DoResponseApp)
server.startServer()