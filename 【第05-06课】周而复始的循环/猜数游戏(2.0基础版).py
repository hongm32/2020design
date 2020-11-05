print('这是一个猜数游戏，数字范围1-50')
set_number = 7  # 设定正确的数
guess_number = input("请输入猜测的数：")  # 提示输入想猜的数
guess_number = int(guess_number)  # 字符串转化为整数
while guess_number != set_number:
    print("抱歉，猜错了！")
    guess_number = int(input("请重新输入猜测的数："))  # 提示输入想猜的数，并转化为整数
print("恭喜你，答对啦！")
input("运行完毕，请按回车键退出...")
