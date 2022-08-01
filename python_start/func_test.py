# 一个简单的计算器
# a = int(input("请输入第一个数："))
# op = input("操作符：")
# b = int(input("请输入第二个数："))
#
#
# def add(a, b):
#     return a + b
#
#
# def sub(a, b):
#     return a - b
#
#
# def div(a, b):
#     return a / b
#
#
# def mul(a, b):
#     return a * b
#
#
# op_dict = {
#     "+": add,
#     "-": sub,
#     "/": div,
#     "*": mul,
# }
# func = op_dict[op]
# print(func(a, b)(a, b))


# 把函数当作普通的变量使用 还可以当作一个返回值 这个特性就是一等公民的特性
# if op == "+":
#     print(a + b)
# elif op == "-"
#     print(a - b)
# elif op == "*"
#     print(a * b)
# elif op == "/"
#     print(a / b)
import threading


# 有一些情况是需要两种操作都出现 1.打开/关闭 文件 2.数据库的连接 (开启 关闭) 3.锁(获取锁 释放锁)
def read_file(file_name):
    f = open(file_name)  # 打开文件成功之后执行逻辑
    with open(file_name, "w") as f:
        sum = 0
        data = [1, 2]
        for line in f:
            sum += int(line)
            # sum += line  # 这一行代码可能有异常 很容易出现异常
        # f.close()
        print("before return ")
        # re_data = data  # 将结果暂存到临时的变量当中去
        re_data = sum  # sum是int 是值传递 将3拷贝到re_data中去 = 3
        lock = threading.Lock()
        lock.acquire()
        try:
            # 此处是多行处理逻辑 这些就可能抛出异常
            pass
        except Exception as e:
            pass
        finally:
            lock.release()
        # 此处跳往 finally 执行
        return re_data
    # except Exception as e:
    #     # f.close()
    #     pass
    # finally:
    #     print("close file")
    #     data.append(3)
    #     f.close()
    #     lock.release  # 此处可能抛出异常
    # 1.代码出现异常 导致 close 执行不到
    # 2.我们忘记close了 无论是否正常运行代码都能够执行到指定逻辑


print(read_file("xxx.txt"))
# 代码很丑陋, 但是一旦逻辑复杂 这种代码大量的充斥了我们的代码中
# 但是 finally有一些细节我们需要知道 就有了一个印象 finally会在return 之后运行
# 事实上真的是这样吗？
# 原因: 实际上finally是在return 之前调用
# finally中是可以return 而且这个地方有了return 就会覆盖原本的return
