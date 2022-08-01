import grpc

from grpc_metadata_test.proto import helloworld_pb2_grpc, helloworld_pb2

# 1. 这个问题能改吗？
# 2. 其他语言有没有这个问题 其他语言 go语言 python不服气
if __name__ == "__main__":
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        hello_request = helloworld_pb2.HelloRequest()
        hello_request.name = "golang"
        response, call = stub.SayHello.with_call(
            # helloworld_pb2.HelloRequest(name='you'),
            hello_request,
            metadata=(
                ('name', 'golang'),
                ('password', 'jetbrains')
            )
        )

        print(response.message)
