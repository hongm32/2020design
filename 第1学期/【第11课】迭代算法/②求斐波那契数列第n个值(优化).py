import time


def fibonacci_iterative(n):
    f1 = f2 = 1
    for i in range(3, n + 1):
        f1, f2 = f2, f1 + f2
    return f2


while True:
    num = input("输入需要计算的月份数：")
    if num.lower() == 'q' or num == "0":
        break
    num = int(num)
    t1 = time.time()
    total = fibonacci_iterative(num)
    t2 = time.time()
    print('用时：{:.12f} 计算出{}月后兔子总对数为：{} '.format(t2 - t1, num, total))
