# P099：计算圆周率
from __future__ import division
import time
# 计算当前时间
time1 = time.time()
# 算法:根据马青公式计算圆周率
while True:
    number = input('请输入想要计算到小数点后的位数:')
    if number.isdigit():
        number = int(number)
        break
# 多计算10位，防止尾数取舍的影响
number1 = number + 10
# 算到小数点后number1位
b = 10 ** number1
# 求含4/5的首项
x1 = b * 4 // 5
# 求含1/239的首项
x2 = b // -239
# 求第一大项
he = x1 + x2
# 设置下面循环的终点，即共计算n项
number *= 2
# 循环初值=3，末值2n,步长=2
for i in range(3, number, 2):
    # 求每个含1/5的项及符号
    x1 //= -25
    # 求每个含1/239的项及符号
    x2 //= -57121
    # 求两项之和
    x = (x1 + x2) // i
    # 求总和
    he += x
# 求出π
pai = he * 4
# 舍掉后十位
pai //= 10 ** 10
# 输出圆周率π的值
paistring = str(pai)
result = paistring[0] + str('.') + paistring[1:len(paistring)]
print(result)
time2 = time.time()
print(u'总共耗时：{:0.8f}s'.format(time2 - time1))
input("运行完毕，请按回车键退出...")
