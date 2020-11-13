money = 100000  # 本金100000
year = 0  # 理财年数赋初值为0
while money >= 0:
    money = round(money * (1 + 0.037), 2) - 20000  # 计算新的理财金额
    year += 1  # 理财年数加1
print(year, "年后资金被全部取出")  # 输出结果

input("运行完毕，请按回车键退出...")
