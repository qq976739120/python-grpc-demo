# -*- coding: utf8 -*-
from concurrent import futures
import time
import grpc
import helloworld_pb2
import helloworld_pb2_grpc
# 实现 proto 文件中定义的 GreeterServicer
class Greeter(helloworld_pb2_grpc.GreeterServicer):
    # 实现 proto 文件中定义的 rpc 调用
    def SayHello(self, request, context):
        return helloworld_pb2.HelloReply(message = 'hello {msg}'.format(msg = request.name))

    def SayHelloAgain(self, request, context):
        return helloworld_pb2.HelloReply(message='hello {msg}'.format(msg = request.name))

def serve():
    # 启动 rpc 服务
    #多线程服务
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    #注册本地服务
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    #监听端口
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(60*60*24) # one day in seconds
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()