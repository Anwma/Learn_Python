# 封装问题
# 栈
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


# 既然有了列表为什么我们还要基于list去实现一个栈呢？
# - 随机获取数据 l[0] - 很有可能误操作 都达不到我们想要的栈的效果
# 上边的类 封装了变量 - list以及基于这些变量的方法 go如果想要达到这个封装效果 那么就一定要解决1.变量的封装 2.方法的封装

# 另外一个场景 我们现在有一组课程的信息需要保存 一门课程有 课程名 课程的url 课程的价格
class Courese:
    def __init__(self, name, price, url):
        self.name = name
        self.price = price
        # self._url = url  # 大家都认可的一种编码规范 这种权限级别的控制 java是可以做到的
        self.__url = url  # 大家都认可的一种编码规范 这种权限级别的控制 java是可以做到的


courses = []
course1 = Courese("django", 100, "https://www.imooc.com")
# print(course1._url)  # 保护成员的访问类 _url
# print(course1.__url)
courses.append(course1)

course2 = Courese("scrapy", 100, "https://www.imooc.com")
courses.append(course2)

# 如果我们仅仅只关心数据的话,还有另一种数据结构更合适,tuple更省内存 性能更高
course2 = []
new_course1 = ("django", 100, "https://www.imooc.com")
course2.append(new_course1)

from collections import namedtuple

# namedtuple很像是一个只能封装数据的类 但是namedtuple的性能比class高 内存比class小很多
NewCourse = namedtuple('Course', 'name price url')
a = NewCourse(name="django", price=100, url="https://www.imooc.com")
print(a.price)
course2.append(a)
# go语言的struct更像是namedtuple 尽量配置简单的语法尽量猜测你的意图
name = ""  # 对空字符串 判断是false情况
name = None
name = 0
name = []
if name:
    print("yes")
s = Stack()
# python中一切皆对象
print(Stack.isEmpty(s))


# s.isEmpty() => Stack.isEmpty(s)
class Course:
    def __init__(self, name, price, url):
        self.name = name
        self.price = price
        self.url = url

    def set_price(self, price):
        self.price = price


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("姓名:{}, 年龄:{}".format(self.name, self.age))


class Student(Person):
    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.school = school

    def detail(self):
        print("姓名:{}, 年龄:{},学校:{}".format(self.name, self.age, self.school))


# 方法和函数 差异并不大
c = Course("django", 100, "https://www.imooc.com")
c.set_price(200)
print(c.price)

s = Student("anwma", 22, "慕课网")
s.speak()
s.detail()
