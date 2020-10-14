def fun(n):
    s = 0
    for i in range(1, n + 1):
        s = s + 1 / i
    return s


print('这是一个有关累加问题1+1/2+1/3+1/4+……1/n的程序')
num = int(input("请输入整数n的值："))
print("1 + 1/2 + … + 1/{} = {}".format(num, fun(num)))
input("运行完毕，请按回车键退出...")
