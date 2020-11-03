# CH4.3-P101利用二分法查数字
x = int(input("请输入要查找的1000以内的整数:"))
step = 0
flag1 = 1
flag2 = 1000
while flag1 <= flag2:
    mid = (flag1 + flag2) // 2
    step = step + 1
    if mid > x:
        flag2 = mid - 1
    elif mid < x:
        flag1 = mid + 1
    else:
        break
print("查找次数为：", step)
input("运行完毕，请按回车键退出...")
