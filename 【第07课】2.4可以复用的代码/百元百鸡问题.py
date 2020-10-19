# 今有鸡翁一，值钱伍；
# 鸡母一，值钱三；
# 鸡鶵三，值钱一。
# 凡百钱买鸡百只，问鸡翁、母、鶵各几何？


def bj(amount=100, num=100):
    for x in range(int(num / 5)):
        for y in range(int(num / 3)):
            z = num - x - y
            if z % 3 == 0 and x * 5 + y * 3 + z / 3 == amount:
                print("公鸡:{}; 母鸡:{}; 小鸡:{}".format(x, y, z))


# 输出
bj(100, 100)
