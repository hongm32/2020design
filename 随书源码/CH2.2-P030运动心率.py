age = float(input('请输入age='))
HRrest = float(input('请输入HRrest='))
low = (220 - age - HRrest) * 0.6 + HRrest
high = (220 - age - HRrest) * 0.8 + HRrest
print("最适宜的心率是：", low, "~", high)
input("运行完毕，请按回车键退出...")
