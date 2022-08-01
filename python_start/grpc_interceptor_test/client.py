import grpc

from grpc_hello.proto import helloworld_pb2_grpc, helloworld_pb2
from datetime import datetime


# 1. 这个问题能改吗？
# 2. 其他语言有没有这个问题 其他语言 go语言 python不服气
class DefaultInterceptor(grpc.UnaryUnaryClientInterceptor):

    def intercept_unary_unary(self, continuation, client_call_details, request):
        start = datetime.now()
        rsp = continuation(client_call_details, request)
        print((datetime.now() - start).microseconds / 1000)
        return rsp


if __name__ == "__main__":
    default_interceptor = DefaultInterceptor()
    with grpc.insecure_channel("localhost:50051") as channel:
        intercept_channel = grpc.intercept_channel(channel, default_interceptor)
        stub = helloworld_pb2_grpc.GreeterStub(intercept_channel)
        hello_request = helloworld_pb2.HelloRequest()
        hello_request.name = "bobby"
        rsp: helloworld_pb2.HelloReply = stub.SayHello(hello_request)

        print(rsp.message)
