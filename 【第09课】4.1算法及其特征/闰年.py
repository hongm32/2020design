# 闰年
# 从2000年到2050年，哪些年份是闰年？
# 能够被4整除但不能被100整除的是闰年
# 能够被400整除的也是闰年
for number in range(2000, 2051):
    if number % 400 == 0:
        print(number)
    elif number % 4 == 0 and number % 100 != 0:
        print(number)

input("运行完毕，请按回车键退出...")
