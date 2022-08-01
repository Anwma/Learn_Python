import sys

a = 20


def myfunc():
    # python中没有定义变量的说法
    global a
    # 修改全局变量
    a = 10
    print(a)


def myfunc2():
    sex = "Male"
    print("Female")
    # 运行中才会发现很多问题，有很多问题会在你的程序已经部署到生产环境中运行到某些逻辑之下才会出现
    out_str = ""
    if sex == "Male":
        out_str = "性别：男"
    print(out_str)


if __name__ == "__main__":
    # myfunc()  # 局部
    # print(a)  # 全局
    # myfunc2()
    # print(bin(2))
    # print(oct(2))
    # print(hex(2))
    # print(ord("a"))
    # print(ord("吴"))
    age = 18
    # 对于python来说，int占用字节是动态的，python的int我们不用担心超过上限
    print(sys.getsizeof(age))
    print(sys.getsizeof(71.2))
    # print("a" + 1)  # "a"表示字符 单引号不代表字符
    