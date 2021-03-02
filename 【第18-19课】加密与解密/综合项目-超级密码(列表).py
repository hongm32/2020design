import tkinter
import datetime


def jiemi():
    d1 = datetime.datetime.now()
    p = varin.get()
    s = [] * 4
    for a in range(33, 127):
        s[0] = chr(a)
        for b in range(33, 127):
            s[1] = chr(b)
            for c in range(33, 127):
                s[2] = chr(c)
                for d in range(33, 127):
                    s[3] = chr(d)
                    if ''.join(s) == p:
                        d2 = datetime.datetime.now()
                        d = d2 - d1
                        varout.set(str(d.seconds) + "秒" + str(d.microseconds / 1000) + "毫秒")
                        return 0  # 起结束函数运行的作用


root = tkinter.Tk()
root.title("破解超级密码")
root.geometry('300x100')
varin = tkinter.StringVar()
varout = tkinter.StringVar()
frame = tkinter.Frame(root)
frm_L = tkinter.Frame(frame)
tkinter.Label(frm_L, text='输入密码：', font=('Arial', 10)).pack()
tkinter.Label(frm_L, text='破解用时：', font=('Arial', 10)).pack()
frm_L.pack(side=tkinter.LEFT)
frm_R = tkinter.Frame(frame)
tkinter.Entry(frm_R, textvariable=varin).pack()
tkinter.Entry(frm_R, textvariable=varout).pack()
frm_R.pack(side=tkinter.RIGHT)
frame.pack()
tkinter.Button(root, text="破解", command=jiemi, relief="solid", width=10).pack()
root.mainloop()
