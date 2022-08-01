import grpc

from grpc_hello.proto import helloworld_pb2_grpc, helloworld_pb2

# 1. 这个问题能改吗？
# 2. 其他语言有没有这个问题 其他语言 go语言 python不服气
if __name__ == "__main__":
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        hello_request = helloworld_pb2.HelloRequest()
        hello_request.name = "bobby"
        # Errors : Assignment not allowed to repeated field "id" in protocol message object.
        hello_request.id.extend([1, 2])
        hello_request.id.append(3)

        # rsp: helloworld_pb2.HelloReply = stub.SayHello(helloworld_pb2.HelloRequest(name="Jeff", id=[1, 2]))
        rsp: helloworld_pb2.HelloReply = stub.SayHello(hello_request)

        print(rsp.message)
