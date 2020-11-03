import random
print('这是一个猜数游戏，数字范围1-50')
set_number = random.randint(1, 50)
flag = False
for times in range(5):
    guess_number = int(input("请输入猜测的数："))
    if guess_number > set_number:
        print("很遗憾，你猜大了")
    elif guess_number < set_number:
        print("抱歉，猜小了")
    if guess_number == set_number:
        flag = True
        break
print('')
if flag:
    print("预测{}次，你猜中了！".format(times + 1))
else:
    print("预测{}次，你还未猜中！".format(times + 1))
input("运行完毕，请按回车键退出...")
