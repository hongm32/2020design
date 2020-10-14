# 4.2.4：最大公约数
def fun1(p, q):
    # 辗转相除法
    temp = p % q
    while temp != 0:
        p = q
        q = temp
        temp = p % q
    return q


def fun2(p, q):
    # 辗转相减法
    while p != q:
        if p > q:
            p = p - q
        else:
            q = q - p
    return q


def fun3(p, q):
    # 枚举法
    hcf = 0
    if p > q:
        smaller = q
    else:
        smaller = p
    for i in range(1, smaller + 1):
        if (p % i == 0) and (q % i == 0):
            hcf = i
    return hcf


def fun4(p, q):
    # 欧几里得算法（辗转相除的递归实现）
    if q == 0:
        return p
    return fun4(q, p % q)


while True:
    a = input("输入第一个正数：")
    if a.isdigit():
        a = int(a)
        break
while True:
    b = input("输入第二个正数：")
    if b.isdigit():
        b = int(b)
        break

print("辗转相除法", fun1(a, b))
print("辗转相减法", fun2(a, b))
print("枚举法", fun3(a, b))
print("欧几里得算法", fun4(a, b))
input("运行完毕，请按回车键退出...")
