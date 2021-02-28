from tkinter import *
import datetime
import random
import string


class MyIterator():
    # 单位字符集合
    letters = string.ascii_lowercase + string.digits  # 小写字母+数字
    min_digits = 0
    max_digits = 0

    def __init__(self, min_digits, max_digits):
        # 实例化对象时给出密码位数范围，一般4到10位
        if min_digits < max_digits:
            self.min_digits = min_digits
            self.max_digits = max_digits
        else:
            self.min_digits = max_digits
            self.max_digits = min_digits

    # 迭代器访问定义
    def __iter__(self):
        return self

    def __next__(self):
        rst = str()
        for item in range(0, random.randrange(self.min_digits, self.max_digits+1)):
            rst += random.choice(MyIterator.letters)
        return rst


# 将时间转化为天时分秒格式
def time_to_hms(_time):
    _s = _time.seconds
    ms = _time.microseconds // 1000  # 毫秒
    d = _s // 86400  # 天（每天86400秒）
    h = _s % 86400 // 3600  # 小时
    m = _s % 3600 // 60  # 分钟
    s = _s % 60  # 秒
    if d > 0:
        return "{}天{:0>2}时{:0>2}分{:0>2}秒{:0>3}毫秒".format(d, h, m, s, ms)
    elif h > 0:
        return "{}时{:0>2}分{:0>2}秒{:0>3}毫秒".format(h, m, s, ms)
    elif m > 0:
        return "{}分{:0>2}秒{:0>3}毫秒".format(m, s, ms)
    elif s > 0:
        return "{}秒{:0>3}毫秒".format(s, ms)
    return "{}毫秒".format(ms)


def jiemi():
    d1 = datetime.datetime.now()  # 获取当前系统时间d1
    p = varin.get()  # 获取输入文本框的数字密码
    if len(p) < 1 or len(p) >= 10:
        varout.set("Error Input")
        return
    for i in MyIterator(len(p), len(p)):
        if i == p:  # 如果密码相同
            d2 = datetime.datetime.now()  # 获取当前系统时间d2
            d = d2 - d1  # 取得时间差
            # 在输出文本框中显示解密用时
            vartime.set(time_to_hms(d))
            varout.set(i)
            break


root = Tk()
root.geometry('300x100')
root.title("数据安全性测试")
frm = Frame(root)
# left
frm_L = Frame(frm)
Label(frm_L, text='输入密码：', font=('Arial', 10)).pack()
Label(frm_L, text='破解用时：', font=('Arial', 10)).pack()
Label(frm_L, text='你的密码是：', font=('Arial', 10)).pack()
frm_L.pack(side=LEFT)

# right
frm_R = Frame(frm)
varin = StringVar()
vartime = StringVar()
varout = StringVar()
Entry(frm_R, show='*', textvariable=varin).pack()
Entry(frm_R, textvariable=vartime, state="disabled").pack()
Entry(frm_R, textvariable=varout, state="disabled").pack()
frm_R.pack(side=RIGHT)
frm.pack()

Button(root, text="破解", command=jiemi, relief="solid", width=10).pack()
root.mainloop()
