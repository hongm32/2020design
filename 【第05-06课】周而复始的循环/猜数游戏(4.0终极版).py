import random


print("########  猜数字小游戏   #########")
print("    1.根据提示猜测50以内数字")
print("    2.输入非数字计输错一次")
print("    3.猜错5次游戏自动退出")
print("#################################")
set_number = random.randint(1, 50)
number_min = 1
number_max = 50
times = 0
for times in range(5):
    try:
        guess_number = int(input("请输入猜测的数({}-{})：".format(number_min, number_max)))
    except NameError and ValueError:
        guess_number = -1
    if guess_number == -1:
        print("输入内容必须为整数！")
    elif guess_number > set_number:
        print("很遗憾，你猜大了")
        number_max = guess_number - 1
    elif guess_number < set_number:
        print("抱歉，猜小了")
        number_min = guess_number + 1
    else:
        print("预测{}次，你猜中了！".format(times + 1))
        break
else:
    print("预测{}次，你还未猜中！".format(times + 1))
input("运行完毕，请按回车键退出...")
