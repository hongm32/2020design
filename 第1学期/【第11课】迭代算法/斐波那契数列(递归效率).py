# 兔子问题
# 假设一对兔子每个月可以生一对小兔子，一对小兔子出生后第2个月就开始生小兔子。
# 则一对兔子一年内能繁殖成多少对？10年呢？
import time


def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


for num in range(16, 41):
    t1 = time.time()
    total = fibonacci(num)
    t2 = time.time()
    print('用时：{:.12f} 计算出{}月后兔子总对数为：{} '.format(t2 - t1, num, total))
input("运行完毕，请按回车键退出...")
