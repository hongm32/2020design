# 鸡兔同笼问题
print('这是一个有关鸡兔同笼问题的程序')
heads = int(input('请输入总的头数:'))
legs = int(input('请输入总的脚数:'))
for chicken in range(1, heads):
    rabbit = heads - chicken
    if 2 * chicken + 4 * rabbit == legs:
        print('鸡有:', chicken, '只')
        print('兔子有:', rabbit, '只')
input("运行完毕，请按回车键退出...")
