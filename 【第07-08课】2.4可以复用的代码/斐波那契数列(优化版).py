# 兔子问题
# 假设一对大兔子每个月可以生一对小兔子，一对小兔子出生后需1个月长大为大兔子。
# 则一对小兔子一年内能繁殖成多少对？10年呢？

def fib(n):
    f1 = f2 = 1
    for i in range(3, n + 1):
        f1, f2 = f2, f1 + f2
    return f2


def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


num = int(input('输入需要计算的月份数：'))
print('兔子总对数为：', fib(num))
input("运行完毕，请按回车键退出...")
