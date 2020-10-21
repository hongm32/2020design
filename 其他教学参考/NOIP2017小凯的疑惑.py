"""
CCF全国信息学奥林匹克联赛(NOIP2017)复赛提高组day1小凯的疑惑
【问题描述】
    小凯手中有两种面值的金币，两种面值均为正整数且彼此互素。每种金币小凯都有无数个。在不找零的情况下，仅凭这两种金币，
有些物品他是无法准确支付的。现在小凯想知道在无法准确支付的物品中，最贵的价值是多少金币？注意：输入数据保证存在小凯无法
准确支付的商品。
【输入格式】
    输入文件名为math.in
    输入数据仅一行，包含两个正整数a和b，它们之间用一个空格隔开，表示小凯手中金币面值。
【输出格式】
    输出文件名为math.out
    输出文件仅一行，一个正整数N，表示不找零的情况下，小凯用手中的金币不能准确支付的最贵的物品的价值。
【输入输出样例】
math.in    math.out
3 7        11
【说明】
本程序输入直接用变量，输出用Print
"""


# 先找出能凑出来的金额
def search_combination(a, b):  # 输入a,b 两个互素的面值
    c = 1  # 从1开始找出能凑出的金额
    while True:  # 不断循环，电脑配置低的，请远离，前方危险
        for i in range(c):
            an01 = a * i
            for j in range(c):
                an02 = b * j
                if an01 + an02 == c:  # 一旦找到能凑出当前金额c的i和j，打印出来
                    print(c, "=", a, '*', i, '+', b, '*', j)
                    # print(c,end='  ')
        c += 1  # 金额不断上涨，上不封顶
        if c > 100:
            break


# 找出两数乘积范围内的可组合数据
def get_combination(a, b):
    c = a * b
    my_list = []  # 创建存放所有组合出来的金额值
    # 找寻过程 -- 不断对比
    for i in range(0, c):
        an01 = a * i
        for j in range(c):
            an02 = b * j
            if an01 + an02 <= c:  # 只找在乘积范围内的组合，节省运算次数
                my_list.append(an01 + an02)  # 将符合的金额添加进目标列表
    return list(set(sorted(my_list)))  # 返回经过去重和排序的目标列表


# 找到最大的那个不能组合的金额
def get_max(a, b):
    my_list = get_combination(a, b)  # 调用找可拼凑数据函数得到目标列表
    my_list.sort(reverse=True)  # 将目标列表反序排列
    # 判断目标列表是否连续，并输出断点数中的最大值
    y = my_list[0] + 1  # 创建对比参数
    for x in my_list:
        if x + 1 != y:
            # print(x, y)
            break
        y = x
    return y - 1  # 返回最大断点值


if __name__ == "__main__":
    # search_combination(3, 7)  # 可以发现，不可组合的面值均集中在靠前的位置，但有多靠前，具体又在哪个位置呢？姑且假定这个数字就在 两数的乘积 之内
    print(get_max(3, 7))
    # 不知道大家有没有发现一个问题，这个最大不可组合数据似乎有一定的规律，规律为：
    #  c = a * b - a - b
    # 这个公式可是一个牛哄哄的定理，名字叫：赛瓦维斯特定理
    # 已知a,b为大于1的正整数，(a,b)=1, 则使不定方程 ax+by=c 无负整数解的最大整数c=ab−a−b
    # 其中的 (a,b) 表示a和b的最大公约数
