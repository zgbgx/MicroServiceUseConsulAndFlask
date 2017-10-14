from server import HttpServer
from httpapp import AppServer
server=HttpServer('127.0.0.1',8001,'127.0.0.1',8500,AppServer)
server.startServer()