from tkinter import *
import tkinter.messagebox


def caesar_cipher1():  # “加密”按钮激发函数
    c = mingwen.get("0.0", "end")[:-1]
    if c == '':
        tkinter.messagebox.showinfo('恺撒密码', '请输入明文。')
        return
    b = ""
    miwen.config(state="normal")
    miwen.delete("0.0", "end")
    for i in range(len(c)):
        if 'a' <= c[i] <= 'w' or 'A' <= c[i] <= 'W':
            b = b + chr(ord(c[i]) + 3)
        elif 'x' <= c[i] <= 'z' or 'X' <= c[i] <= 'Z':
            b = b + chr(ord(c[i]) - 23)
        else:
            b = b + c[i]
    miwen.insert("0.0", b)
    miwen.config(state="disabled")


def caesar_cipher2():  # “解密”按钮激发函数
    c = miwen.get('0.0', 'end')[:-1]
    if c == '':
        tkinter.messagebox.showinfo('恺撒密码', '请单击“加密”按钮。')
        return
    b = ''
    mingwen2.config(state="normal")
    mingwen2.delete('0.0', 'end')
    for i in range(len(c)):
        if 'd' <= c[i] <= 'z' or 'D' <= c[i] <= 'Z':
            b += chr(ord(c[i]) - 3)
        elif 'a' <= c[i] <= 'c' or 'A' <= c[i] <= 'C':
            b += chr(ord(c[i]) + 23)
        else:
            b += c[i]
    mingwen2.insert('0.0', b)
    mingwen2.config(state="disabled")


def caesar_cipher3():  # “对比”按钮激发函数
    b = mingwen.get('0.0', 'end')[:-1]
    c = mingwen2.get('0.0', 'end')[:-1]
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


root = Tk()
root.title("恺撒加密")
root.geometry('300x330')
Label(root, text='请输入明文', font=('Arial', 10)).pack()
mingwen = Text(root, width=300, height=4)
mingwen.pack()
mingwen.focus_set()
Button(root, text="加密", command=caesar_cipher1, relief="solid", width=10).pack()
Label(root, text='恺撒密文', font=('Arial', 10)).pack()
miwen = Text(root, width=300, height=4)
miwen.pack()
Button(root, text='解密', command=caesar_cipher2, relief='solid', width=10).pack()
Label(root, text='解密得到的凯撒明文', font=('Arial', 10)).pack()
mingwen2 = Text(root, width=300, height=4, state="disabled")
mingwen2.pack()
Button(root, text='对比', command=caesar_cipher3, relief='solid', width=10).pack()
root.mainloop()
