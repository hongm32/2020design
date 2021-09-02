# 寻找1000以内的所有素数(质数)


def is_prime(n):
    """判断是否质数"""
    if n == 2:
        return 1
    if n <= 1:
        return 0
    for div in range(3, n):
        if n % div == 0:
            return 0
    return 1


def prime(number):
    prime_list = []
    for i in range(2, number + 1):
        if is_prime(i):
            prime_list.append(i)
    return prime_list


print(prime(1000))
input("运行完毕，请按回车键退出...")
