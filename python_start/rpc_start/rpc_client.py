# requests
import requests
import json


# 自己实现了一个demo级别的rpc封装 代理
# 将url映射到对应的函数 urlconfig route装饰器 call id 的映射
# 序列化 反序列化
class ClientStub:
    def __init__(self, url):
        self.url = url

    def add(self, a, b):
        # 1.call id
        # 2.序列化和反序列化
        # 3.传输协议 http
        rsp = requests.get(f"{self.url}/?a={a}&b={b}")
        return json.loads(rsp.text).get("result", 0)


# 这不就是写一个web服务器 无非就是自己封装一下client
# 不想知道过多的细节 只想像本地一样调用
client = ClientStub("http://127.0.0.1:8003")
print(client.add(1, 2))
print(client.add(3, 4))
# rsp = requests.get("http://127.0.0.1:8003/?a=1&b=2")
# http的调用 1.每个函数调用我们都得记住 url地址 参数是如何传递的 返回数据如何解析的
# add函数调用就像本地函数调用
# print(rsp.text)
