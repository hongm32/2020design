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


print(prime(100))
