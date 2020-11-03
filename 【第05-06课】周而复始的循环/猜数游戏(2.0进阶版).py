import random
print('这是一个猜数游戏，数字范围1-50')
set_number = random.randint(1, 50)  # 随机设定正确的数
guess_number = input("请输入猜测的数：")  # 提示输入想猜的数
guess_number = int(guess_number)  # 字符串转化为整数
while guess_number != set_number:
    if guess_number > set_number:  # 比较猜的数与目标数：大了
        print("很遗憾，你猜大了")
    else:  # 比较猜的数与目标数：小了
        print("抱歉，猜小了")
    guess_number = int(input("请重新输入猜测的数："))  # 提示输入想猜的数，并转化为整数
print("恭喜你，答对啦！")
input("运行完毕，请按回车键退出...")
