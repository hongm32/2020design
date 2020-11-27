# 尝试用二分法求解方程x**3-X**2-x-1=0

def f(x):
    return x ** 3 - x ** 2 - x - 1  # 【补】函数表达式，提醒幂用**#


while True:
    # 要保证 f(x1) * f(x2) < 0 才能确认方程在(x1, x2)内有解
    x1 = float(input("请输入有解单调区间左边界："))
    x2 = float(input("请输入有解单调区间右边界："))
    if f(x1) * f(x2) <= 0:
        break
    else:
        print("输入的区间可能无解！")
x0 = None
while abs(x2 - x1) >= 1e-13:
    x0 = (x1 + x2) / 2
    if f(x1) * f(x0) < 0:  # 函数f在（x1, x0)有解
        x2 = x0
    if f(x2) * f(x0) < 0:  # 函数f在（x0, x2)有解
        x1 = x0
    if f(x0) == 0:  # x0为解，直接跳出循环
        break

print("方程解为：", x0)
input("运行完毕，请按回车键退出...")
