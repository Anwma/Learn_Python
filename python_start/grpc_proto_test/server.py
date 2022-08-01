from concurrent import futures

import grpc

from grpc_proto_test.proto import hello_pb2, hello_pb2_grpc
# from google.protobuf.empty_pb2 import Empty
from grpc_proto_test.proto.hello_pb2 import HelloReply

# from grpc_proto_test.proto.base_pb2 import Pong

result = HelloReply.Result()


# pong = hello_pb2.base__pb2.Pong()


class Greeter(hello_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return hello_pb2.HelloReply(message=f"姓名,{request.name},url:{request.url}")


if __name__ == "__main__":
    #     1.实例化server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # 2.注册逻辑到server中
    hello_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    # 3.启动server
    server.add_insecure_port('[::]:50053')
    server.start()
    server.wait_for_termination()
