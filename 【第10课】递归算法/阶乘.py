# 求阶乘

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# 调用阶乘函数
total = factorial(10)
print("10!=", total)
input("运行完毕，请按回车键退出...")
