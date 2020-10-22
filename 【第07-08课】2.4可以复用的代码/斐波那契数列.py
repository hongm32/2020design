# 兔子问题
# 假设一对兔子每个月可以生一对小兔子，一对小兔子出生后第2个月就开始生小兔子。
# 则一对兔子一年内能繁殖成多少对？10年呢？

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


num = int(input('输入需要计算的月份数：'))
print('兔子总对数为：', fibonacci(num))
input("运行完毕，请按回车键退出...")
