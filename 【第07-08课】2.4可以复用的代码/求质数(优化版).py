import math
import time


# 返回所有质数
def prime(number):
    prime_list = []
    for i in range(2, number + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            prime_list.append(i)
    return prime_list


# 返回所有质数(优化)
def prime_optimize(number):
    if number < 2:
        return []
    else:
        prime_list = [2]
    for i in range(3, number + 1, 2):  # 优化2：除2外，偶数不是质数
        for j in range(2, int(math.sqrt(i)) + 1):  # 优化1：如果n不是质数, 则n有满足1<d<=sqrt(n)的因子d
            if i % j == 0:
                break
        else:
            prime_list.append(i)
    return prime_list


n = 50000
t0 = time.time()
l1 = prime(n)
t1 = time.time()
l2 = prime_optimize(n)
t2 = time.time()
print(l1[:10], len(l1) if l1 == l2 else "Error!")
print("优化前：{}".format(t1-t0))
print("优化后：{}".format(t2-t1))
