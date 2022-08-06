import logging
import signal
import os
import sys
import argparse
import socket
from concurrent import futures
from functools import partial
from loguru import logger

import grpc

BASE_DIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
sys.path.insert(0, BASE_DIR)

from user_srv.proto import user_pb2_grpc, user_pb2
from user_srv.handler.user import UserServicer
from common.grpc_health.v1 import health_pb2_grpc, health_pb2
from common.grpc_health.v1 import health
from common.register import consul
from user_srv.settings import settings


def on_exit(signo, frame):
    logger.info("进程中断")
    sys.exit(0)


def get_free_tcp_port():
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp.bind(("", 0))
    _, port = tcp.getsockname()
    tcp.close()
    return port


def serve():
    parser = argparse.ArgumentParser()
    parser.add_argument('--ip',
                        nargs="?",
                        type=str,
                        default="192.168.245.1",
                        help="binding ip"
                        )
    parser.add_argument('--port',
                        nargs="?",
                        type=int,
                        default=50051,
                        help="the listening port"
                        )
    args = parser.parse_args()
    logger.add("logs/user_srv_{time}.log")

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # 注册用户服务
    user_pb2_grpc.add_UserServicer_to_server(UserServicer(), server)
    # 注册健康检查
    health_servicer = health.HealthServicer()
    health_pb2_grpc.add_HealthServicer_to_server(health_servicer, server)

    server.add_insecure_port(f'{args.ip}:{args.port}')
    """
        windows下支持的信号是有限的：
            SIGINT ctrl+c 中断
            SIGTERM kill发出的软件终止
    """
    # 主进程退出信号监听
    signal.signal(signal.SIGINT, on_exit)
    signal.signal(signal.SIGTERM, on_exit)

    logger.info(f"启动服务：{args.ip}:{args.port}")
    server.start()
    logger.info(f"服务注册开始")
    register = consul.ConsulRegister(settings.CONSUL_HOST, settings.CONSUL_PORT)
    # 没有注册成功
    if not register.register(name=settings.SERVICE_NAME, id=settings.SERVICE_NAME,
                             address=args.ip, port=args.port, tags=settings.SERVICE_TAGS, check=None):
        logger.info(f"服务注册失败")
        sys.exit(0)
    logger.info(f"服务注册成功")

    server.wait_for_termination()


# @logger.catch
# def my_function(x, y, z):
#     # An error? It's caught anyway!
#     return 1 / (x + y + z)


if __name__ == "__main__":
    # my_function(0,0,0)
    # logger.debug("调试信息")
    # logger.info("普通信息")
    # logger.warning("警告信息")
    # logger.error("错误信息")
    # logger.critical("严重错误信息")
    logging.basicConfig()
    serve()
