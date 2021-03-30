money = 0  # 初值为0
for i in range(10):
    money = round((money + 20000) / (1 + 0.037), 2)  # 计算理财金额
print("初期投资", money, "元")  # 输出结果

input("运行完毕，请按回车键退出...")
