# 寻找1000以内的所有素数(质数)

def prime(number):
    prime_list = []
    for i in range(2, number + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            prime_list.append(i)
    return prime_list


print(prime(1000))
input("运行完毕，请按回车键退出...")
