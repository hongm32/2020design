def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)

n = int(input("请输入需要计算的月份数："))
print("兔子总数为：", fib(n))

