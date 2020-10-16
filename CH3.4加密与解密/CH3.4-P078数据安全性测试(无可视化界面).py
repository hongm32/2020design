import datetime


# 开始
p = int(input('请输入p='))
d1 = datetime.datetime.now()
d = None
for i in range(p + 1):
    if i == p:
        d2 = datetime.datetime.now()
        d = d2 - d1
        print(str(d.seconds) + "秒" + str(d.microseconds / 1000) + "毫秒")
input("运行完毕，请按回车键退出...")
