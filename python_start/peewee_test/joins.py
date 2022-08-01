import datetime

from peewee import *
import logging

logger = logging.getLogger("peewee")
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

db = MySQLDatabase('peewee', host='127.0.0.1', user='root', passwd='anwma')


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    username = TextField()

    class Meta:
        table_name = 'user2'


class Tweet(BaseModel):
    content = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)
    user = ForeignKeyField(User, backref="tweets")

    class Meta:
        table_name = 'tweet2'


class Favorite(BaseModel):
    user = ForeignKeyField(User, backref='favorites')
    tweet = ForeignKeyField(Tweet, backref='favorites')


# 数据准备
def populate_test_data():
    data = (
        ('huey', ('meow', 'hiss', 'purr')),
        ('mickey', ('woof', 'whine')),
        ('zaizee', ())
    )

    for username, tweets in data:
        user = User.create(username=username)
        for tweet in tweets:
            Tweet.create(user=user, content=tweet)

    # Populate a few favorites for our users,such that:
    favorite_data = (
        ('huey', ['whine']),
        ('mickey', ['purr']),
        ('zaizee', ['meow', 'purr'])
    )
    for username, favorites in favorite_data:
        user = User.get(User.username == username)
        for content in favorites:
            tweet = Tweet.get(Tweet.content == content)
            Favorite.create(user=user, tweet=tweet)


if __name__ == "__main__":
    db.connect()
    db.create_tables([User, Tweet, Favorite])
    # 正向取
    # for tweet in Tweet.select():
    #     print(tweet.content, tweet.user.username)
    #
    # populate_test_data()

    # 使用表链接
    # ('SELECT `t1`.`id`, `t1`.`content`, `t1`.`timestamp`, `t1`.`user_id` FROM `tweet2` AS `t1` INNER JOIN
    # `user2` AS `t2` ON (`t1`.`user_id` = `t2`.`id`) WHERE (`t2`.`username` = %s)', ['mickey'])
    # select * from user2 join tweet2 on user2.id=tweet2.user_id where user2.username='mickey'
    # print(query.sql())
    # query = Tweet.select().join(User).where(User.username == 'mickey')
    # for q in query:
    #     print(q.user.username, q.content)

    # query = Tweet.select(Tweet, User.username).join(User, on=(Tweet.user == User.id)).where(User.username == "mickey")
    # for q in query:
    #     print(q.user.username, q.content)

    # 反向
    # user = User.get(User.username == "mickey")
    # tweets = Tweet.select().where(Tweet.user == user)
    # for tweet in tweets:
    #     print(user.username, tweet.content)

    # 反向2
    # tweets = User.get(User.username == "mickey").tweets
    # tweets = Tweet.select().where(Tweet.user == user)
    # for tweet in tweets:
    #     print(tweet.content)

    # 想得到5个数据 会发起5次请求
    # for tweet in Tweet.select():
    #     print(tweet.content, tweet.user.username)

    # 什么时候sql会发起请求 以及会发起多少次请求 开发人员来说 很重要 很多sql不会喜欢用orm的原因
    # query = Tweet.select(Tweet, User.username).join(User).where(User.username == "mickey")
    # for q in query:
    #     print(q.user.username, q.content)
