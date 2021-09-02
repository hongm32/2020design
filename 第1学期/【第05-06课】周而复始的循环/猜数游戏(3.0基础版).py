import random
print('这是一个猜数游戏，数字范围1-50')
set_number = random.randint(1, 50)
guess_number = -1
for times in range(5):
    guess_number = int(input("请输入猜测的数："))
    if guess_number > set_number:
        print("很遗憾，你猜大了")
    elif guess_number < set_number:
        print("抱歉，猜小了")
    if guess_number == set_number:
        break
if guess_number == set_number:
    print("你猜中了！")
else:
    print("你还未猜中！")
input("运行完毕，请按回车键退出...")
