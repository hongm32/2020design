def shengxiao(year):
    # 求生肖
    zodiac = ["鼠", "牛", "虎", "兔", "龙", "蛇", "马", "羊", "猴", "鸡", "狗", "猪"]
    index = (year - 1972) % 12
    return zodiac[index]


# 以下为主程序
myyear = int(input("请输入出生年份,输入0结束:"))
while myyear != 0:
    print("你的生肖是:", shengxiao(myyear))
    myyear = int(input("请输入出生年份，输入0结束:"))
