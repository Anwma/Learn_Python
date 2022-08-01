import requests

# rsp = requests.post("http://127.0.0.1:8083/form_post", data={
#     "message": "你好",
#     "nick": "jeff"
# })
# print(rsp.text)

rsp = requests.post("http://127.0.0.1:8083/post?id=1&page=2", data={
    "name": "你好",
    "message": "jeff"
})
print(rsp.text)
