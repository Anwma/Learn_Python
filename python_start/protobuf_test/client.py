import json

from protobuf_test.proto import hello_pb2

# 生成的pb文件不要去改
requests = hello_pb2.HelloRequest()
requests.name = "Jeff"
res_str = requests.SerializeToString()
print(len(res_str))  # len = 6
res_json = {
    "name": "Jeff"
}
print(len(json.dumps(res_json)))  # len = 16

# b'\n\x04Jeff'

# 如何通过字符串反向生成对象
requests2 = hello_pb2.HelloRequest()
requests2.ParseFromString(res_str)
print(requests2.name)

# 和json对比一下
