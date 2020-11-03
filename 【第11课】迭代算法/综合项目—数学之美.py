def f(a):
    # 定义f(x)函数，计算f(x)=x5+x4+x-10
    return a ** 5 + a ** 4 + a - 10


def f1(a):
    # 定义f(x)函数，求导数f1(x)= 5*x4+4*x3+1
    return 5 * (a ** 4) + 4 * (a ** 3) + 1


# 设置初始值
x = 1
x1 = 2   # x1的初值只要确保|x-x1|>1e-10就可以
print('迭代过程中的x值：')
# 根据迭代公式计算
while abs(x - x1) > 1e-10:
    x1 = x
    y1 = f(x)
    y2 = f1(x1)
    x = x1 - y1 / y2
    print(x)
print('近似解：', x)  # 输出最后解
