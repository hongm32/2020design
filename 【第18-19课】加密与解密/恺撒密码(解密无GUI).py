c = input("请输入密文:")
b = ""
for i in range(0, len(c)):                          # 获取密文内容的每一个字母，并破解
    if 'd' <= c[i] <= 'z' or 'D' <= c[i] <= 'Z':    # 判断d-z或D-Z间的字母
        b = b + chr(ord(c[i]) - 3)                  # 破解密文
    elif 'a' <= c[i] <= 'c' or 'A' <= c[i] <= 'C':  # 判断a-c或A-C间的字母
        b = b + chr(ord(c[i]) + 23)                 # 破解密文
    else:
        b = b + c[i]                                # 字母以外的密文不变
print("你的明文为:" + b)
