# 玩转汉诺塔(Hanoi)游戏_移动次数


def hanoi(n):
    if n == 1:
        return 1
    return 2 * hanoi(n - 1) + 1


total = hanoi(64)
print("需要移动{}次，约{}亿年".format(total, total/3600/24/365/1e8))
input("运行完毕，请按回车键退出...")
