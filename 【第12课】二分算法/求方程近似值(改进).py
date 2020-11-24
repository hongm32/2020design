# 4.3.5：P105-拓展练习2-求方程近似值
# 尝试用二分法求解方程x^3-X^2+x-1=0

def f1(x):
    return x ** 3 - x ** 2 + x - 2


def fun(f, x1, x2):
    # 二分法求函数f的近似解
    x0 = (x1 + x2) / 2
    while x2 - x1 >= 1e-13:
        x0 = (x1 + x2) / 2
        if f(x1) * f(x0) < 0:  # 函数f在（x1, x0)有解
            x2 = x0
        elif f(x2) * f(x0) < 0:  # 函数f在（x0, x2)有解
            x1 = x0
    return x0


# 要保证 f(a) * f(b) < 0 才能确认方程在(a, b)内有解
a = -100000
b = 3000000
mid = fun(f1, a, b)

print("方程解为：", mid)
input("运行完毕，请按回车键退出...")
