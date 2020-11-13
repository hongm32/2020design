num = int(input("请输入感冒指数： "))
if 0 <= num <= 6 :
    print("少发")
elif 7<= num <= 19:
    print("较易发")
elif 20 <= num <= 30:
    print("易发")
elif 31 <= num <= 61:
    print("极易发")
else:
    print("指数值不正确")

input("运行完毕，请按回车键退出...")
