principal = 50000  # 本金50000元
rate = 0.0325  # 1年定期利率3.25%
year = 5  # 存款期限
money = principal * (1 + rate) ** year  # 计算存款总额
print("5年以后存款总额：", money, "元")  # 输出结果

input("运行完毕，请按回车键退出...")
