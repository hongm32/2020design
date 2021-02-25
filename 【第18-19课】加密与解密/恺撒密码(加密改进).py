from tkinter import *       # 导入tkinter模块


def new_caesar():    # “加密”按钮激发函数
    t = mingwen.get("0.0", "end")[:-1]
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
    miwen.insert("0.0", z)


m = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n = 'QWERTYUIOPASDFGHJKLZXCVBNM'

root = Tk()
root.title("凯撒加密（改进）")
root.geometry('300x200')
Label(root, text='请输入明文', font=('Arial', 10)).pack()
mingwen = Text(root, width=300, height=4)
mingwen.pack()
mingwen.focus_set()
Button(root, text="加密", command=new_caesar, relief="solid", width=10).pack()
Label(root, text='凯撒密文', font=('Arial', 10)).pack()
miwen = Text(root, width=300, height=4)
miwen.pack()
root.mainloop()
