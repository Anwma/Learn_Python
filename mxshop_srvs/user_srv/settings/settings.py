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

DB = ReconnectMySQLDatabase(database=MYSQL_DB, host=MYSQL_HOST, port=MYSQL_POST, user=MYSQL_USER, password=MYSQL_PASSWORD)
