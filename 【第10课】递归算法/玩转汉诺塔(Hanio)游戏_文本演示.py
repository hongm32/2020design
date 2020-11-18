# 玩转汉诺塔(Hanio)游戏_文本演示


def hanno(k, s, m, t):
    # 定义一个函数,k层塔，将盘子从s借助m移动到t
    global Step
    if k == 1:
        Step += 1
        print(Step, s, '-->', t)  # 将一个盘子从s移动到t
    else:
        hanno(k-1, s, t, m)  # 将前n-1个盘子从s移动到m上
        Step += 1
        print(Step, s, '-->', t)  # 将最底下的最后一个盘子从s移动到t上
        hanno(k-1, m, s, t)  # 将m上的n-1个盘子移动到t上


# 主程序
while True:
    n = input('请输入汉诺塔的层数：')
    if n.lower() == 'q':
        exit()
    elif n.isdigit():
        n = int(n)
        break

Step = 0
hanno(n, 'A', 'B', 'C')
input("运行完毕，请按回车键退出...")
