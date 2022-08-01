# 1. 定义并生成表
import datetime

from peewee import *
import logging

logger = logging.getLogger("peewee")
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

db = MySQLDatabase('peewee', host='127.0.0.1', user='root', passwd='anwma');


class User(Model):
    # 如果没有设置主键 那么自动生成一个id的主键
    username = CharField(primary_key=True, max_length=20)
    age = CharField(default=18, max_length=20, verbose_name="年龄")

    # max_length = 20不起作用，因为是建立表，不是修改表
    # 修改表用：migrations,
    class Meta:
        database = db


class Tweet(Model):
    user = ForeignKeyField(User, backref='tweets')
    message = TextField()
    created_date = DateTimeField(default=datetime.datetime.now)
    is_published = BooleanField(default=True)

    class Meta:
        database = db


if __name__ == "__main__":
    # 1.生成表结构
    # db.connect()
    # db.create_tables([User, Tweet])

    # 2.添加
    # charlie = User(username="charlie")  # update set age = 18 where username ="charlie"
    # rows = charlie.save()
    # if rows == 0:
    #     print("未更新数据")
    # charlie.save(force_insert=True)  # 1.save方法既可以完成新建. 也可以完成更新的操作（你的对象钟主键值是否有设置你是一个更新的操作）

    # huey = User.create(username="huey")

    # 3.查询
    # 3.1 get方法
    #   1.返回回来的是直接的user对象
    #   2.这个方法如果查询不到会抛出异常
    try:
        # charlie = User.get(User.username == "charlie")
        charlie = User.get_by_id("chalie")
        print(charlie.username)
    # 这个操作发起的sql请求是什么
    except User.DoesNotExist as e:
        print("查询不到")
    # 3.2 select操作 查询所有
    # users = User.select()
    #   1.没有看到sql查询语句,用于组装sql
    #   2.对象是 ModelSelect 对象 我们对 ModelSelect 进行for循环和切片的时候才会发起请求

    # print(users.sql())
    # print(type(users))
    # user = users[0]
    # print(type(user))

    # usernames = ["charlie", "huey", "mickey"]
    # users = User.select().where(User.username.in_(usernames))
    # for user in users:
    #     print(user.username)
    # for user in User.select():
    #     print(user.username)

    # 更新
    charlie = User(username="charld2ie")  # update set xx=xx where username="charlie"
    print(charlie.save())
    # 使用update更新
    print(User.update(age=15).where(User.username == "charlie").execute())

    # 删除数据
    user = User.get(User.username == "charld2ie")
    user.delete_instance()

    # 是不是这个语句也不会执行 确实没执行 要使用其 execute()方法
    # query = User.delete().where(User.username == "charlie").execute()
    # print(query)

    # 有少数的方法会直接执行sql语句 get get_by_id

# 使用 primary_key=True 报错
# Traceback (most recent call last):
#   File "D:/JetbrainsCode/Pycharm/PythonStart/peewee_test/model_define.py", line 36, in <module>
#     charlie.save()  # 1.save方法既可以完成新建. 也可以完成更新的操作
#   File "C:\Users\Wozen\Envs\python_start\lib\site-packages\peewee.py", line 6691, in save
#     raise ValueError('no data to save!')
# ValueError: no data to save!

