def leijia(n):
    s = 0
    for i in range(1, n + 1):
        s = s + 1 / i
    return s

s1 = leijia(5)
s2 = leijia(10000)
print(s1, s2)

input("运行完毕，请按回车键退出...")
