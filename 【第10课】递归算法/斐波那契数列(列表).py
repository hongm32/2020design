# 兔子问题
# 假设一对兔子每个月可以生一对小兔子，一对小兔子出生后第2个月就开始生小兔子。
# 则一对兔子一年内能繁殖成多少对？10年呢？

def fib(n):
    fib_list = []
    for i in range(n):
        if i <= 1:
            fib_list.append(1)
        else:
            fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list


while True:
    num = int(input('输入需要计算的月份数：'))
    if num == 0:
        break
    print('兔子总对数为：{}'.format(fib(num)[-1]))
