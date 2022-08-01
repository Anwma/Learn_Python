# import requests
#
# # 这是一个http的库 发送出去的文本都是http协议的文本
# requests.get("", json={})

# 使用socket 编程
# import json
# import socket
#

# client = socket.create_connection(("localhost", 1234))
# client.sendall(json.dumps(request).encode())
# # 获取服务器返回的数据
# rsp = client.recv(1024)
# rsp = json.loads(rsp.decode())
# print(rsp["result"])
import requests

request = {
    "id": 0,
    "params": ["jeff"],
    "method": "HelloService.Hello"
}
rsp = requests.post("http://localhost:1234/jsonrpc", json=request)
print(rsp.text)
