#
from typing import List
from copy import deepcopy


def print_list(course: List[str]):
    course[0] = "bobby"
    print(course)


# 引用传递
course = ["django", "scrapy", "tornado", "python", "golang"]
# 深拷贝 浅拷贝
# print_list(deepcopy(course))
# print(type(course))
sub_course = course[1:4]  # 左闭右开的区间[1:4] 新的list 底层的数据是复制出来的
my_list = list
sub_course[0] = "imooc"
print(sub_course)
print(type(sub_course))
print(course)  # src_arr 不被影响到
# print(type(sub_course))
# print(course)

# if "scrapy" in course:  # 内部无非就是实现了一个魔法方法 __contains__
#     print("yes")
a = [1, 2, 3]
b = a[:]
b[0] = 8
print(a)
print(b)

m = {
    "a": "va",
    "b": "vb"
}
a = None
b = None

print_list(id(a), id(b))
print(m.get("d", "wozen"))
if "a" in m:
    print("yes")
