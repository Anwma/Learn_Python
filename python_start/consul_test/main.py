import requests

headers = {
    "contentType": "application/json"
}


def register(name, id, address, port):
    url = "http://192.168.119.128:8500/v1/agent/service/register"
    rsp = requests.put(url, headers=headers, json={
        "Name": name,
        "ID": id,
        "Tags": ["mxshop", "bobby", "imooc", "web"],
        "Address": address,
        "Port": port,
        "Check": {
            "GRPC": f"{address}:{port}",
            "GRPCUseTLS": False,  # 不需要做安全验证
            "Timeout": "5s",
            "Interval": "5s",
            "DeregisterCriticalServiceAfter": "15s",
        }

    })
    if rsp.status_code == 200:
        print("注册成功")
    else:
        print(f"注册失败: {rsp.status_code}")


def deregistry(id):
    url = f"http://192.168.119.128:8500/v1/agent/service/deregister/{id}"
    rsp = requests.put(url, headers=headers)
    if rsp.status_code == 200:
        print("注销成功")
    else:
        print(f"注销失败: {rsp.status_code}")


def filter_service(name):
    url = "http://192.168.119.128:8500/v1/agent/services"
    params = {
        "filter": f'Service == "{name}"'
    }
    rsp = requests.get(url, params=params).json()
    for key, value in rsp.items():
        print(key)
    # print(rsp)


if __name__ == "__main__":
    # register("mxshop-web", "mxshop-web", "192.168.245.1", 50051)
    # deregister("mxshop-web")
    rsp = filter_service("user-srv")
