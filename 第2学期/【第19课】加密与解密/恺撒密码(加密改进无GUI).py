#  开始
def new_caesar(m, n, t):
    z = ''
    i = 0
    while i < len(t):
        tmp = t[i].upper()
        if tmp in m:
            if ord(t[i]) <= 90:
                z += n[m.find(tmp)]
            else:
                z += n[m.find(tmp)].lower()
        else:
            z += t[i]
        i += 1
    return z


m0 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n0 = 'QWERTYUIOPASDFGHJKLZXCVBNM'
a = input('请输入<明文>a=')
b = new_caesar(m0, n0, a)
print('对应的密文为:', b)
c = new_caesar(n0, m0, b)
print('解密后明文为:', c)
if a == c:
    print('加密解密成功！')
else:
    print('加密解密失败！')
input("运行完毕，请按回车键退出...")
