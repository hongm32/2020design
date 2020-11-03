# 水仙花数
# “水仙花数”是指一个三位自然数，其各位数字的立方和等于该数本身。
# 编程输出所有的水仙花数，每行一个。
# 例如153是“水仙花数”，因为153=1^3+5^3+3^3

def resolve(number):
    # 使用整除获取各位数字
    digit_sum = 0
    while number:
        digit_sum += (number % 10) ** 3
        number //= 10
    return digit_sum


for i in range(100, 1000):
    if resolve(i) == i:
        print(i)

input("运行完毕，请按回车键退出...")
