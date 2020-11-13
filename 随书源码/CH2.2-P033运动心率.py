age = float(input("请输入年龄Age="))
hrrest = float(input("请输入安静心率HRrest="))
gender = input("请输入male或female：")
if gender == "male":
    n = 220
else:
    n = 210
low = (n - age - hrrest) * 0.6 + hrrest
high = (n - age - hrrest) * 0.8 + hrrest
# 输出最适宜运动心率的范围
print('最适宜的运动心率是：', low, '~', hight)

input("运行完毕，请按回车键退出...")
