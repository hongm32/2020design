money = 50000  # 本金50000元
rate = [0.0325, 0.03, 0.03, 0.02, 0.0175]  # 利率列表
for i in rate:
    money = round(money * (1 + i), 2)  # 计算每年存款额
print("5年以后存款总额：", money, "元")  # 输出结果

input("运行完毕，请按回车键退出...")
