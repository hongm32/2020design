# 今有鸡翁一，值钱伍；
# 鸡母一，值钱三；
# 鸡鶵三，值钱一。
# 凡百钱买鸡百只，问鸡翁、母、鶵各几何？


def hundred_chickens(amount=100, num=100):
    for x in range(num // cock_price + 1):
        for y in range(num // hen_price + 1):
            z = num - x - y
            money = x * cock_price + y * hen_price + z / chick_count
            if z % chick_count == 0 and money == amount:
                print("公鸡:{}; 母鸡:{}; 小鸡:{}".format(x, y, z))


cock_price = 5  # 公鸡价格5文
hen_price = 3  # 母鸡价格3文
chick_count = 3  # 3只小鸡1文
# 输出
hundred_chickens(100, 100)
input("运行完毕，请按回车键退出...")
