# 错误和异常
# 除法函数
def div(a, b):
    # 稍微认真一点的程序员都会在除法中判断我们的被除数 b 是否为0
    if b == 0:
        # raise Exception("被除数不能为0")  # 异常
        return None, "被除数不能为0"
    # dict访问了一个不存在的key, 在list中对空的list进行了data[0]
    user_info_dict = {
        "name": "wozen",
        "age": 18
    }
    if "weight" in user_info_dict:
        user_info_dict["weight"]
    # 如果每个地方都这样写,代码中的if就太多了,那就是你的bug问题,这种问题就一定要早发现
    return a / b, None


# 如果你的这个函数 - div返回的是None 这个时候调用者不会出问题
# 错误和异常 错误就是可以预先知道的出错情况 这个时候我们把这个情况叫做错误
# 不可预知的问题叫做异常 程序员写的代码不严谨造成了某个地方产生了异常

def cal():
    while 1:
        a = int(input())
        b = int(input())
        v, err = div(a, b)
        if err is not None:
            print(err)
        else:
            print(v)
        # try:
        #     div(a, b)
        # except Exception as e:
        #     print(e)
    # 后面还有逻辑
    # 被调用函数传递的异常会导致我们的cal函数出现异常


# cal()
import re

desc = "wozen:22"
m = re.match("wozen:(.*)", desc)
if m is not None:
    print(m.group(1))
