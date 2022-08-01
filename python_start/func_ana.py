from typing import get_type_hints, Iterable, MutableMapping
from functools import wraps
from inspect import getfullargspec


# 函数参数和返回值的类型声明
# import socket
#
# s = socket.socket()
# s.send()


def add2(a: int, b: float = 3.5) -> float:
    return a + b


def validate_input(obj, **kwargs):
    hints = get_type_hints(obj)
    for para_name, para_type in hints.items():
        if para_name == "return":
            continue
        if not isinstance(kwargs[para_name], para_type):
            raise TypeError("参数：{} 类型错误,应该是：{}".format(para_name, para_type))


def type_check(decorator):
    @wraps(decorator)
    def wrapped_decorator(*args, **kwargs):
        func_args = getfullargspec(decorator)[0]
        kwargs.update(dict(zip(func_args, args)))

        validate_input(decorator, **kwargs)
        return decorator(**kwargs)

    return wrapped_decorator


@type_check
def add(a: int, b: int) -> int:
    return a + b


# 调用的时候才能发现类型问题

if __name__ == "__main__":
    # print(add(1, 2))
    # print(add2(1))
    # 有些人还并不满意
    # print(add("bobby:", "18"))
    #
    # print(get_type_hints(add))
    # print(add.__annotations__)
    # print(bin(13))
    # name = "wozen:楚心云"
    # print(name[2])
    # print(len("wozen:楚心云"))
    # in可以用在很多地方
    # if "wozen" in name:
    #     print("yes")
    #
    # name.index("w")
    # name.count("b")
    # name.startswith("b")
    # name.endswith("云")
    # print("hello".upper())
    # print("HELLO".lower())
    # print("hello world".split())
    # print(",".join(["hello", "world"]))
    # name = "wozen"
    # age = 18
    # print("name: %s,age: %d" % (name, age))
    # print("name:{},age:{}".format(name, age))
    # print(f"name:{name},age:{age}")

    # name = input("请输入你的姓名: ")
    # print(name)
    #
    # age = int(input("请输入你的年龄: "))
    # print(type(age))
    # sum = 0
    # python中对于for的用法很统一
    # for i in range(1, 11):
    #     sum += i
    # print(sum(range(1, 11)))
    # print(sum)
    # for item in "bobby":
    #     print(item)
    for index, item in enumerate("bobby"):
        print(index, item)

    name = "hello:我的世界"
    print(name[6])
