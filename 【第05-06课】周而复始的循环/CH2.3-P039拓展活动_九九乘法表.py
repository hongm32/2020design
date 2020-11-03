for i in range(1, 10):
    for j in range(1, i + 1):
        print("{0:1}*{1:1}={2:2}  ".format(j, i, j*i), end="")  # 按格式输出
    print()  # 换行

input("运行完毕，请按回车键退出...")
