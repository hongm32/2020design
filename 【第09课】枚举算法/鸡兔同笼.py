# 鸡兔同笼问题
print('这是一个有关鸡兔同笼问题的程序')
for chicken in range(1, 35):
    for rabbit in range(1, 35):
        if chicken + rabbit == 35 and 2 * chicken + 4 * rabbit == 94:
            print('鸡有:', chicken, '只')
            print('兔子有:', rabbit, '只')
input("运行完毕，请按回车键退出...")
