# “百鸡百钱”问题
# 是一个有名的数学问题，出自《张丘建算经》。其内容是：
# 公鸡5文钱1只，
# 母鸡3文钱1只，
# 小鸡3只1文钱，
# 用100文钱买100只鸡，其中公鸡、母鸡和小鸡都必须有，
# 问公鸡、母鸡和小鸡各多少只？

money = 100  # 一共100文钱
num = 100  # 一共100只鸡
cock_price = 5  # 公鸡价格5文
hen_price = 3  # 母鸡价格3文
chick_price = 3  # 3只小鸡1文
for cock_num in range(1, money // cock_price + 1):  # 公鸡只数可能为1-20
    for hen_num in range(1, money // hen_price + 1):  # 母鸡只数可能为1-33
        chick_num = num - cock_num - hen_num  # 小鸡数量
        money1 = cock_num * cock_price + hen_num * hen_price + chick_num / chick_price
        if money1 == money:
            print("公鸡:{: >2} 母鸡:{: >2} 小鸡:{}".format(cock_num, hen_num, chick_num))

input("运行完毕，请按回车键退出...")
