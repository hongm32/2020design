# 游戏介绍：
# 狼羊菜过河，一人要将一狼、一羊、一棵白菜这些东西都运送到河对岸。
# 渡船太小，一次只能带一样。
# 因为狼要吃羊，羊会吃白菜，所以狼和羊，羊和白菜不能在无人监视的情况下相处。
# 你能做到么？


def insertq(m, i):
    global rear
    if m not in Q:
        rear += 1
        Q.append(m)
        F.append(front)
        L.append(i)


def outputr(f):
    global n
    if F[f] > 0:
        outputr(F[f])
    if L[f] >= 0:
        n += 1
        print(n, ":", law[L[f]])


def ok(mi, wi, si, vi):
    return wi != si and si != vi or mi == si


Q = [0]
F = [0]
L = [-1]
law = ["移动人", "移动人和狼", "移动人和羊", "移动人和菜"]
front = 0
rear = 0
x = 0
while front <= rear:
    x = Q[front]
    if x == 15:
        break
    V = x % 2
    S = x // 2 % 2
    W = x // 4 % 2
    M = x // 8
    if ok(1-M, W, S, V):
        x = (1 - M) * 8 + W * 4 + S * 2 + V
        insertq(x, 0)
    if M == W and ok(1 - M, 1 - W, S, V):
        x = (1 - M) * 8 + (1 - W) * 4 + S * 2 + V
        insertq(x, 1)
    if M == S and ok(1 - M, W, 1 - S, V):
        x = (1 - M) * 8 + W * 4 + (1 - S) * 2 + V
        insertq(x, 2)
    if M == V and ok(1 - M, W, S, 1 - V):
        x = (1 - M) * 8 + W * 4 + S * 2 + (1 - V)
        insertq(x, 3)
    front += 1
if x == 15:
    print("成功！")
    n = 0
    outputr(front)
else:
    print("无法完成任务！")
