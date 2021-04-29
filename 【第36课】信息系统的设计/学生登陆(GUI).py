import os
import tkinter as tk
import tkinter.messagebox


win1 = tk.Tk()
win1.title("登录界面")
win1.geometry('350x400')
win1.resizable(0, 0)
varl1 = tk.StringVar()
varl2 = tk.StringVar()
button1 = tk.StringVar()
# 在窗口上创建两个标签
tk.Label(win1, text="学号", width=14).grid(row=1, column=0)
tk.Label(win1, text="密码", width=14).grid(row=2, column=0)
# 在窗口上创建两个输入框
tk.Entry(win1, textvariable=varl1, width=20).grid(row=1, column=1)
tk.Entry(win1, textvariable=varl2, width=20, show="*").grid(row=2, column=1)
# 在窗口上创建一个按钮
tk.Button(win1, command=button1, text="登录", relief="solid", width=15).grid(row=3, column=1)
# 进入事件循环
win1.mainloop()
