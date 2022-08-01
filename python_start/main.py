# from collections import namedtuple
# def main():
#     print("hello", end="")
#     print(" python", end="")
#
#
# if __name__ == '__main__':
#     # main()
#     # 定义匿名变量
#     my_list = ["bobby", "imooc", "test"]
#     for _, item in enumerate(my_list):
#         print(item)
#     # 元组 (无法被修改)
#     sex_tuple = ("male", "female")

from calc.add import add1 as add1_int
from calc.add_float import add1

print(add1(1, 2))
print(add1_int(1, 2))
# python中没有package说明自己属于什么package 和包名 和文件名称是挂钩的
