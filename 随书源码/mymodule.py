def match_num(num):
    f = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]  # 0-9的数字分别需要多少根小棒
    if num == 0:  # 火柴棒总数变量赋初值
        total = f[0]
    else:
        total = 0
    while num > 0:
        x = num % 10  # 取num除以10的余数，即num的个位数
        total += f[x]  # 所需火柴棒数累加
        num = num // 10	 # num整除10，即去掉num的个位数
    return total  # 返回需要多少根火柴棒数
