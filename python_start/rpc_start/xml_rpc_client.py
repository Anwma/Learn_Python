from xmlrpc import client

# xml-rpc挺好用的 和我们调用 django 的服务器 对于 django 这种web框架来说一定是可以做到xml-rpc
# django 的目的不是这种
# requests 调用 http postman
# rpc 强调的是本地调用效果
# rpc 在内部调用很多
server = client.ServerProxy("http://localhost:8088")
print(server.add(2, 3))
print(server.subtract(2, 3))
