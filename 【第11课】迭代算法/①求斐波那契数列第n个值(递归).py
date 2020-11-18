import time


def fibonacci_recursive(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


while True:
    num = input("输入需要计算的月份数：")
    if num.lower() == 'q':
        break
    num = int(num)
    t1 = time.time()
    total = fibonacci_recursive(num)
    t2 = time.time()
    print('用时：{:.12f} 计算出{}月后兔子总对数为：{} '.format(t2 - t1, num, total))
