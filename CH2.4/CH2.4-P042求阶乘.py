def factorial(n):
    # 求n!
    s = 1
    for i in range(2, n + 1):
        s = s * i
    return s


# 调用factorial函数
total = factorial(4)
print(total)

input("运行完毕，请按回车键退出...")
