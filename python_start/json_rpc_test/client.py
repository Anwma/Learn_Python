import jsonrpclib
import threading
import time


def request():
    server = jsonrpclib.ServerProxy('http://localhost:8080')
    print(server.add(2, 3))


for i in range(10):
    thread = threading.Thread(target=request)
    thread.start()

time.sleep(30)
# print(server.add(2, 3))
