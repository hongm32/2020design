from tkinter import *       # 导入tkinter模块
import tkinter.messagebox   # 弹窗库


def caesar_cipher():                   # “解密”按钮激发函数
    c = miwen.get('0.0', 'end')[:-1]    # 获取miwen对象的内容（密文）
    if c == '':
        tkinter.messagebox.showinfo('恺撒密码', '请单击“加密”按钮。')
        return
    b = ''
    mingwen2.config(state="normal")    # 允许mingwen2对象可操作
    mingwen2.delete('0.0', 'end')      # 清空mingwen2对象的内容
    for i in range(len(c)):            # 获取密文内容的每一个字符，并解密
        if 'd' <= c[i] <= 'z' or 'D' <= c[i] <= 'Z':    # 判断d～z或D～Z间的字母
            b += chr(ord(c[i]) - 3)                     # 生成明文
        elif 'a' <= c[i] <= 'c' or 'A' <= c[i] <= 'C':  # 判断a～c或A～C间的字母
            b += chr(ord(c[i]) + 23)              # 生成明文
        else:
            b += c[i]                           # 字母以外的密文不变
    mingwen.insert('0.0', b)                   # 在mingwen2对象中显示解密结果
    mingwen.config(state="disabled")           # 锁定mingwen2对象为不可操作


def caesar_cipher3():                     # “对比”按钮激发函数
    b = mingwen.get('0.0', 'end')[:-1]   # 获取mingwen对象的内容（初始明文）
    c = mingwen2.get('0.0', 'end')[:-1]  # 获取mingwen2对象的内容（解密得到的明文）
    if b == '':
        tkinter.messagebox.showinfo('恺撒密码', '请输入明文。')
        return
    if c == '':
        tkinter.messagebox.showinfo('恺撒密码', '请单击“解密”按钮。')
        return
    if b == c:
        tkinter.messagebox.showinfo('恺撒密码', '解密正确！')
    else:
        tkinter.messagebox.showinfo('恺撒密码', '解密错误！')


root = Tk()                 # 建立一个窗口
root.title("恺撒解密")        # 设置窗口标题
root.geometry('300x200')    # 设置窗口大小
Label(root, text='请输入恺撒密文', font=('Arial', 10)).pack()
miwen = Text(root, width=300, height=4)
miwen.pack()
miwen.focus_set()    # 获得焦点
Button(root, text='解密', command=caesar_cipher, relief='solid', width=10).pack()
Label(root, text='解密得到的凯撒明文', font=('Arial', 10)).pack()
mingwen = Text(root, width=300, height=4, state="disabled")
mingwen.pack()
root.mainloop()
