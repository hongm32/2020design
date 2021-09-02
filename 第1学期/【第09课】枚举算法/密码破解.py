# 密码破解
# 小明淘气，他给爸爸的行李箱设了一个四位整数密码，
# 他告诉爸爸：“个位是2，十位是1，百位是3-5，千位是0-6，该密码能被7整除，能被8整除，且能被9整除”，
# 你能通过编程帮小明爸爸解开行李箱密码吗？

digit1 = 2
digit2 = 1
for digit3 in [3, 4, 5]:
    for digit4 in range(7):
        digit = digit4 * 1000 + digit3 * 100 + digit2 * 10 + digit1
        if digit % 7 == 0 and digit % 8 == 0 and digit % 9 == 0:
            print("Great! The digit is:", digit)

input("运行完毕，请按回车键退出...")
