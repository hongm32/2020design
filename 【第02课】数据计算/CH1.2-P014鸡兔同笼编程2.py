# 枚举法
print('这是一个有关鸡兔同笼问题的程序')
heads = int(input('请输入总的头数:'))
legs = int(input('请输入总的脚数:'))
for tu in range(heads + 1):
    if tu * 4 + (heads - tu) * 2 == legs:
        print('兔子有:', tu, '头')
        print('鸡有:', int(heads - tu), '头')
input("运行完毕，请按回车键退出...")
