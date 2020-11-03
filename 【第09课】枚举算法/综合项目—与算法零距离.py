# 活动：安排住宿
# 活动描述：有n个男生一起出去旅游，要安排酒店住宿，
# 已知4人间为140元/间，3人间为120元/间，
# 那怎样订房间最省钱，而且要保证每人都有床位。

n = int(input("输入人数："))
minimum = 1000000  # 最小值赋初值
minimum_r4 = minimum_r3 = 0
for r4 in range(n // 4 + 1):  # 罗列4人间房间数量
    rs = n - 4 * r4  # 计算剩余人数
    if rs % 3 == 0:  # 计算剩余人数需要多少个3人间
        r3 = rs // 3
    else:
        r3 = rs // 3 + 1
    w = 140 * r4 + 120 * r3  # 计算费用
    if minimum > w:
        minimum = w  # 保存最少费用
        minimum_r4 = r4
        minimum_r3 = r3
print("费用总计：{}元".format(minimum))
print("其中需要订4人间:{}间 ".format(minimum_r4))
print("        3人间:{}间 ".format(minimum_r3))
