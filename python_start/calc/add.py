__all__ = ("name",)  # 通过all的方式决定暴露哪一些变量或者说函数 但是只能够影响from * 的这种用法
name = "wozen"


def add1(x: int, y: int) -> int:
    return x + y
