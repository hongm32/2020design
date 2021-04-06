"""
查找LuckNumber:给定一个数字n，寻找不小于n的最小目标数。
目标数的要求是:因数只有奇质数，并且所有因数不重复。最后各（因数-1）也能被（目标数-1）整除。
    任何质数都不是目标数，因为质数的因数只有它本身和1。
    数字6=2×3不是目标数，因为存在了一个偶数2。
    数字45=3×3×5不是目标数，因为3出现了2次（不唯一）
    数字15=3×5不是目标数，因为（5-1）不能被（15-1）整除。
    数字10585=5×29×73是一个目标数，因为它所有的质因数（5，29，73）都是奇数并且只出现了一次，而且各个因数减1之后能被（目标数-1）整除。

编写一个函数luck_number(N)，寻找不小于N的最小目标数。测试N=2021时的输出结果。
"""

# import sys
# sys.setrecursionlimit(20000)   # 递归深度


def is_prime(n):
    """判断是否质数"""
    if n == 2:
        return 1
    if n <= 1 or not n % 2:
        return 0
    for div in range(3, int(n ** 0.5) + 1, 2):
        if n % div == 0:
            return 0
    return 1


def get_prime_factor(num, odd):
    if num == 1:
        return prime_list
    for i in range(odd, num + 1):
        if is_prime(i):
            if num % i == 0:
                if i in prime_list:
                    return False
                else:
                    prime_list.append(i)
                    odd = i + 1
                    return get_prime_factor(int(num / i), odd)


def check(n):
    global prime_list
    prime_list = []
    if n % 2 == 0:
        return 0, "存在因数2，不是luck数"
    elif is_prime(n):
        return 0, "是质数，不是luck数"
    else:
        prime_list = get_prime_factor(n, 3)
        # print(n, prime_list)  # 注意NoneType
        if not prime_list:
            return 0, "有重复质因数"
        else:
            for j in prime_list:
                if n % j or (n - 1) % (j - 1):
                    return 0, f"质因数{j}不符合"
        return 1, "luck数"


def lucky_number(n):
    while n:
        result = check(n)
        # print(n, result[1])
        if result[0]:
            print(n)
            break
        n += 1


prime_list = []
N = 2021
lucky_number(N)
