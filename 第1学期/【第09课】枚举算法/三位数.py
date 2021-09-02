# 由1、2、3组成的三位数

print("这是一个由1、2、3组成的三位数的程序")
for a in [1, 2, 3]:
    for b in [1, 2, 3]:
        for c in [1, 2, 3]:
            if a != b and b != c and c != a:
                print("由1、2、3可以组成：{}{}{}".format(a, b, c))

input("运行完毕，请按回车键退出...")
