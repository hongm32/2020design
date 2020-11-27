# 实数a和b满足以下条件：
# 4 ** a + a = 4
# log4b + b = 4
# 求 a + b 的值

import math


def f1(x):
    return 4 ** x + x - 4


def f2(x):
    return math.log(x, 4) + x - 4


def fun(f, x1, x2):
    x0 = None
    while abs(x2 - x1) >= 1e-13:
        x0 = (x1 + x2) / 2
        if f(x1) * f(x0) < 0:  # 函数f在（x1, x0)有解
            x2 = x0
        if f(x2) * f(x0) < 0:  # 函数f在（x0, x2)有解
            x1 = x0
        if f(x0) == 0:
            break
    return x0


a = fun(f1, 0, 1)
b = fun(f2, 1, 4)
print("a + b的值为：{:.1f}".format(a + b))
input("运行完毕，请按回车键退出...")
