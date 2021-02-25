import datetime

print("数据安全性测试小程序(按任意非数字键退出)")
# 开始
while True:
    p = input('请输入p=')
    if p.isdigit():
        p = int(p)
    else:
        break
    d1 = datetime.datetime.now()
    d = None
    for i in range(p + 1):
        if i == p:
            d2 = datetime.datetime.now()
            d = d2 - d1
            print(str(d.seconds) + "秒" + str(d.microseconds / 1000) + "毫秒")
