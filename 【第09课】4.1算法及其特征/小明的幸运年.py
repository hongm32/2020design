# 小明的幸运年
# 老师问小明的年龄，小明说：今年是我的幸运年。我出生年份的四位数字加起来刚好是我的年龄（周岁）。
# 已知今年是2020年，请推断出小明的出生年份（4位整数，默认小明<100岁）。

def resolve(number):
    digit_sum = 0
    while number:
        digit_sum += number % 10
        number //= 10
    return digit_sum


def resolve1(number):
    digit_sum = 0
    for digit in str(number):
        digit_sum += int(digit)
    return digit_sum


for i in range(1921, 2021):
    if resolve(i) == 2020 - i:
        print(i)

input("运行完毕，请按回车键退出...")
