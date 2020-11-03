# 抬脚法P014
print('这是一个有关鸡兔同笼问题的程序')
heads = float(input('请输入总的头数:'))
legs = float(input('请输入总的脚数:'))
tu = int((legs - heads * 2) / (4 - 2))
print('兔子有:', tu, '头')
print('鸡有:', int(heads - tu), '头')
input("运行完毕，请按回车键退出...")
