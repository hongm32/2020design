def divide(_n):
    if _n == 1:
        return 1
    return 2 * divide(_n - 1) + 1


def divide_iterative(_n):
    _sum = 1
    for i in range(2, _n + 1):
        _sum = 2 * _sum + 1
    return _sum


while True:
    n = int(input("需要对折次数："))
    if n == 0:
        break
    print("这{}条直线把平面划分成为 {} 个部分。".format(n, divide(n)))
    # print("这{}条直线把平面划分成为{}个部分。".format(n, divide_iterative(n)))
