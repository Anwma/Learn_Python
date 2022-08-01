# 1. 采用dict映射
def print_A():
    print("A")


def print_B():
    print("B")


def print_C():
    print("C")


def print_D():
    print("D")


score = 90
switch = {
    90: print_A,
    80: print_B,
    70: print_C,
    60: print_D,
}

switch[score]()
