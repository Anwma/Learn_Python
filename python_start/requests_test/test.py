import requests

# rsp = requests.post("http://127.0.0.1:8083/form_post", data={
#     "message": "你好",
#     "nick": "jeff"
# })
# print(rsp.text)

# rsp = requests.post("http://127.0.0.1:8083/post?id=1&page=2", data={
#     "name": "你好",
#     "message": "jeff"
# })
# print(rsp.text)
# from requests_test.proto import user_pb2, user_pb2_grpc
#
# user = user_pb2.Teacher()
#
# rsp = requests.get("http://127.0.0.1:8083/someProtoBuf")
# user.ParseFromString(rsp.content)
# print(user.name, user.course, )

import requests

# 登录
# rsp = requests.post("http://127.0.0.1:8083/loginJSON", json={
#     "user": "b",
#     "password": "imooc",
# })
# print(rsp.text)

# 注册
# rsp = requests.post("http://127.0.0.1:8083/signup", json={
#     "age": 18,
#     "name": "bobby",
#     "email": "13@qq.com",
#     "password": "imooc",
#     "rePassword": "imoocc",
# })
# print(rsp.text)

rsp = requests.get("http://127.0.0.1:8083/ping", headers={
    "x-token": "bobbdy"
})
print(rsp.text)
