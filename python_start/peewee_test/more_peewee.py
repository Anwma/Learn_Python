import datetime

import peewee
from peewee import *

import logging

logger = logging.getLogger("peewee")
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

db = MySQLDatabase('peewee', host='127.0.0.1', user='root', passwd='anwma');


class BaseModel(Model):
    add_time = DateTimeField(default=datetime.datetime.now, verbose_name="添加时间")

    class Meta:
        database = db  # 这里是数据库链接，为了方便建立多个表，可以把这个部分提炼出来形成一个新的类


# class Person(BaseModel):
#     name = CharField(verbose_name='姓名', max_length=10, null=False, index=True)
#     passwd = CharField(verbose_name='密码', max_length=20, null=False, default='123456')
#     email = CharField(verbose_name='邮件', max_length=50, null=False, unique=True)
#     gender = IntegerField(verbose_name='性别', null=False, default=1)
#     birthday = DateField(verbose_name='生日', null=True, default=None)
#     is_admin = BooleanField(verbose_name='是否是管理员', default=True)
#
#     class Meta:
#         table_name = 'person'  # 这里可以自定义表名


class Person(BaseModel):
    first = CharField()
    last = CharField()

    class Meta:
        primary_key = CompositeKey('first', 'last')


class Pet(BaseModel):
    owner_first = CharField()
    owner_last = CharField()
    pet_name = CharField()

    class Meta:
        constraints = [SQL('FOREIGN KEY(owner_first,owner_last) REFERENCES person(first,last)')]


class Blog(BaseModel):
    pass


class Tag(BaseModel):
    pass


# 复合主键
class BlogToTag(BaseModel):
    """A simple "through" table for many-to-many relationship."""
    blog = ForeignKeyField(Blog)
    tag = ForeignKeyField(Tag)

    class Meta:
        primary_key = CompositeKey('blog', 'tag')


class User(BaseModel):
    # 如果没有设置主键 那么自动生成一个id的主键
    username = CharField(max_length=20)
    age = CharField(default=18, max_length=20, verbose_name="年龄")

    class Meta:
        table_name = 'new_user'


if __name__ == "__main__":
    db.connect()
    db.create_tables([Person, Pet, Blog, Tag, BlogToTag, User])

    # id = Person.insert({
    #     'first': 'jeff3',
    #     'last': 'steven3'
    # }).execute()

    # import random
    #
    # for i in range(10):
    #     User.create(username=f"jeff{i}", age=random.randint(18, 40))
    # id = Blog.insert({}).execute()
    # print(id)

    # 我的model中设置的default是当我们让model启动去插入数据的时候

    # blog = Blog()
    # print(blog.id)
    # print(blog.save())
    # print(blog.id)
    # blogs = [{
    #     'add_time': datetime.datetime.now()
    # }, {
    #     'add_time': datetime.datetime.now()
    # }]
    # Blog.insert_many([{
    #
    # }])

    # ('SELECT `t1`.`add_time`, `t1`.`first`, `t1`.`last` FROM `person` AS `t1` WHERE ((%s OR `t1`.`first`) = %s)',
    # ['jeff', 'jeff2'])
    # person = Person.select().where((Person.first == 'jeff') | (Person.first == 'jeff2'))
    # print(person.sql())

    # like查询

    # query = Person.select().where(Person.first.contains('li'))
    # query = Person.select().where(Person.first.startswith('li'))
    # query = Person.select().dicts()
    # for row in query:
    #     print(type(row))
    #     print(row)
    # print(query)

    # person = Person.select().order_by(Person.id.desc())
    # for row in person:
    #     print(row)

    # users = User.select().order_by(User.age.asc())  # 升序 从小到大
    # users = User.select().order_by(User.age.desc())  # 降序
    # users = User.select().order_by(-User.age)  # 降序
    # users = User.select().order_by(User.age)  # 升序 兼容了django

    # distinct 去重 count方法统计数量
    # query = User.select(User.username).distinct().count()
    # for q in query:
    #     print(q.username)
    # print(query)
    # SELECT DISTINCT `t1`.`age` FROM `new_user` AS `t1`
    # select username from new_user where age = (select max(age) from new_user)
    # max_age = User.select(fn.MAX(User.age)).scalar()
    # users = User.select().where(User.age == max_age)
    # for user in users:
    #     print(user.username)
    # print(max_age)
    # for user in users:
    #     print(user)
    # sub_query = User.select(fn.MAX(User.age))
    # query = User.select(User.username).where(User.age == sub_query)
    # for q in query:
    #     print(q.username)

    # query = User.raw('SELECT * FROM new_user WHERE username = %s', "jeff0")
    query = User.select().where(SQL('username = "%s"' % "jeff0"))  # "%s"
    for q in query:
        print(q.username, q.age)
