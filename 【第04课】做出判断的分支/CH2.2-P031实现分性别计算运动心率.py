print("男女最适宜运动心率计算器")
age = float(input("请输入年龄="))
hrrest = float(input("请输入安静心率="))
gender = input("请输入male或female：")
n = 220 if gender == "male" else 210
low = (n - age - hrrest) * 0.6 + hrrest
high = (n - age - hrrest) * 0.8 + hrrest
print("最适宜的运动心率是：", low, "-", high)
input("运行完毕，请按回车键退出...")
