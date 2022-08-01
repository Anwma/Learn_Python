# go语言的接口(protol 协议)设计是参考了鸭子类型(python)和java的接口
# 什么是鸭子类型？什么叫协议
# 当看到一只鸟走起来像鸭子、游泳起来像鸭子、叫起来也像鸭子，那么这只鸟就可以被称为鸭子
# 采用的是面向对象的类继承

class Animal:
    def born(self):
        pass

    def walk(self):
        pass


class Dog(Animal):
    def born(self):
        pass

    def walk(self):
        pass


class Cat(Animal):
    pass


dog = Dog()
# dog是不是动物类 实际上dog就是动物类 忽略了鸭子类型 对于用惯面向对象的人来说 这个做法有点古怪
# python语言本身的设计上来说是基于鸭子类型实现的

# dog是本身animal,并不是由继承关系确定的，而是由你的这个类是不是实现了这些方法

# Animal实际上只是定义了一些方法的名称而已 其他任何类 你继不继承只要实现了这个Animal()里面的方法那你这个类就是Animal类型

from typing import Iterable  # 实际上list没有继承 Iterable这个类 好比是一份协议

a = []
print(type(a))
print(isinstance(a, Iterable))  # 这是因为 list里面实现了list方法 魔法方法 只是实现了它的方法
b = tuple()
print(isinstance(b, Iterable))


class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    # 实现以下魔法方法可用for 迭代  不实现会抛异常
    def __iter__(self):
        return iter(self.employee)


# company = Company(["tom", "bob", "jane"])
company = Company([100, 110, 120])
for em in company:
    print(em)
# for语句可以对dict list tuple set等类型进行for循环
# for语句可以对iterable类型进行操作，只要你实现了__iter__那你就可以进行for循环
# 你的类继承了什么不重要 你的类名称不重要 重要的是你实现了什么魔法方法
# if isinstance(company, Iterable):
#     print("company是Iterable类型")
# else:
#     print("company不是Iterable类型")
price = [100, 200, 300]  # python本身是基于鸭子类型设计的一门语言 - 协议最重要
# price = (100, 200, 300)
# print(sum(price))
print(sum(company))
# 强调 什么是鸭子类型 非常推荐大家去好好学习python中的魔法方法
# django + xadmin
# scrapy
