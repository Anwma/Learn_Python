from playhouse.pool import PooledMySQLDatabase
from playhouse.shortcuts import ReconnectMixin


# 使用peewee的连接池 使用 ReconnectMixin 来防止出现连接断开查询失败
# mysql gone away
class ReconnectMySQLDatabase(ReconnectMixin, PooledMySQLDatabase):
    # python的mro
    pass


MYSQL_DB = "mxshop_user_srv"
MYSQL_HOST = "192.168.119.128"
MYSQL_POST = 3306
MYSQL_USER = "root"
MYSQL_PASSWORD = "root"

# consul的配置
CONSUL_HOST = "192.168.119.128"
CONSUL_PORT = 8500

# 服务相关的配置
SERVICE_NAME = "user-srv"
SERVICE_TAGS = ["imooc", "bobby", "python", "srv"]

DB = ReconnectMySQLDatabase(database=MYSQL_DB, host=MYSQL_HOST, port=MYSQL_POST, user=MYSQL_USER,
                            password=MYSQL_PASSWORD)
