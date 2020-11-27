# 4.3.5：P105-拓展练习2-求方程近似值
# 尝试用二分法求解方程x^3-X^2+x-1=0

def f1(x):
    return x ** 3 - x ** 2 - x - 1


def fun(f, x1, x2):
    # 二分法求方程f(x)=0的近似解
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


# 要保证 f(a) * f(b) < 0 才能确认方程在(a, b)内有解
while True:
    # 要保证 f(a) * f(b) < 0 才能确认方程在(a, b)内有解
    a = float(input("请输入有解单调区间左边界："))
    b = float(input("请输入有解单调区间右边界："))
    if f1(a) * f1(b) <= 0:
        break
    else:
        print("输入的区间可能无解！")
mid = fun(f1, a, b)

print("方程解为：", mid)
input("运行完毕，请按回车键退出...")
