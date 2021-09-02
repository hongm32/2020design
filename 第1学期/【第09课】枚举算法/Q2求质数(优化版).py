# 寻找10000以内的所有素数(质数)
import time


def is_prime(n):
    """判断是否质数"""
    if n == 2:
        return 1
    if n <= 1 or not n % 2:
        return 0
    for div in range(3, n):
        if n % div == 0:
            return 0
    return 1


def is_prime_optimize(n):
    """判断是否质数"""
    if n == 2:
        return 1
    if n <= 1 or not n % 2:
        return 0
    for div in range(3, int(n ** 0.5) + 1, 2):  # 优化2：除数到平方根，减少循环次数
        if n % div == 0:
            return 0
    return 1


# 返回所有质数
def prime(number):
    prime_list = []
    for i in range(2, number + 1):
        if is_prime(i):
            prime_list.append(i)
    return prime_list


# 返回所有质数(优化)
def prime_optimize(number):
    if number < 2:
        return []
    else:
        prime_list = [2]
    for i in range(3, number + 1, 2):  # 优化1：除2外，偶数不是质数
        if is_prime_optimize(i):
            prime_list.append(i)
    return prime_list


n = 10000
t0 = time.time()
l1 = prime(n)
t1 = time.time()
l2 = prime_optimize(n)
t2 = time.time()
print(l1[:10], len(l1) if l1 == l2 else "Error!")
print("优化前：{}".format(t1 - t0))
print("优化后：{}".format(t2 - t1))
input("运行完毕，请按回车键退出...")
