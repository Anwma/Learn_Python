import consul
import json
c = consul.Consul(host="192.168.119.128")
address = "192.168.119.129"
port = 50051
check = {
    "GRPC": f"{address}:{port}",
    "GRPCUseTLS": False,  # 不需要做安全验证
    "Timeout": "5s",
    "Interval": "5s",
    "DeregisterCriticalServiceAfter": "15s",
}
rsp = c.agent.service.register(name="user-srv", service_id="user-srv", address=address, port=port,
                               tags=["mxshop"], check=check)
rsp = c.agent.services()
json.loads(rsp)
rsp = c.agent.service.deregister("user-srv")
print(rsp)
