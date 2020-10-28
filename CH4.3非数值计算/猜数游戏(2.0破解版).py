import random
print('这是一个猜数游戏，数字范围1-50')
set_number = random.randint(1, 50)  # 随机设定正确的数
print("当前随机生成的正确的数是:", set_number)
number_min = 1
number_max = 50
step = 1
guess_number = number_min + (number_max - number_min) // 2  # 取中间数
while guess_number != set_number:
    step += 1
    if guess_number > set_number:  # 比较猜的数与目标数：大了
        print("  猜{}，很遗憾，你猜大了".format(guess_number))
        number_max = guess_number - 1
    else:  # 比较猜的数与目标数：小了
        print("  猜{}，抱歉，猜小了".format(guess_number))
        number_min = guess_number + 1
    guess_number = number_min + (number_max - number_min) // 2
print("  猜{}，恭喜你，答对啦！共猜{}次".format(guess_number, step))
input("运行完毕，请按回车键退出...")
