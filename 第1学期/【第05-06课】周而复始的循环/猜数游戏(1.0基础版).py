set_number = 7  # 先设定正确的数字
guess_number = input('请输入你猜的数(1-50):')  # 提示输入想猜的数
guess_number = int(guess_number)  # 将字符型通过int转成整型
if guess_number == set_number:  # 比较猜的数与目标数：对了
    print('恭喜你，答对啦！')
else:  # 比较猜的数与目标数：小了
    print('抱歉，猜错了！')
input("运行完毕，请按回车键退出...")
