print("男女最适宜运动心率计算器")
age = float(input("请输入年龄Age="))
hrrest = float(input("请输入安静心率HRrest="))
ehr = float(input('请输入EHR='))  # 输入运动后的心率
gender = input("请输入male或female：")
if gender == "male":
    n = 220
else:
    n = 210
low = (n - age - hrrest) * 0.6 + hrrest
high = (n - age - hrrest) * 0.8 + hrrest
if ehr < low:
    print('您的运动心率太低，请适当提高')
elif low <= ehr <= high:
    print('您的运动心率正好，请保持')
else:
    print('您的运动心率太高，请适当降低')

input("运行完毕，请按回车键退出...")
