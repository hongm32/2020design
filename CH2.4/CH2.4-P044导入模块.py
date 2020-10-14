import mymodule  # 导入模块
snum = 6  # 6根火柴棒
print("你可以拼出这些数字：")
for i in range(112):
    if mymodule.match_num(i) == snum:  # 调用模块内match_num（）函数
        print(i)
input("运行完毕，请按回车键退出...")
