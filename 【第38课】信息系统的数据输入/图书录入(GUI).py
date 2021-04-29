import os
import tkinter as tk
import tkinter.messagebox
import win32com.client


def Button1():
    ISBN = varl1.get()
    title = varl2.get()
    name = "书名"
    if ISBN == "" or title == "":
        tkinter.messagebox.showerror("错误！", "ISBN和书名都需要进行填写！")
    else:
        sql = "INSERT INTO {}".format(tablename)


conn = win32com.client.Dispatch(r"ADODB.Connection")
DSN = 'PROVIDER = Microsoft.ACE.OLEDB.12.0;DATA SOURCE = 图书借阅管理.mdb'  # Access2007及以后
conn.Open(DSN)

tablename = 'books'

win = tk.Tk()
win.title("图书录入")
win.geometry('350x400')

varl1 = tk.StringVar()
varl2 = tk.StringVar()
varl3 = tk.StringVar()



# 在窗口上创建三个标签
tk.Label(win1, text="原密码", width=14).grid(row=1, column=0)
tk.Label(win1, text="新密码", width=14).grid(row=2, column=0)
tk.Label(win1, text="再输一次新密码", width=14).grid(row=3, column=0)
# 在窗口上创建三个输入框
tk.Entry(win1, textvariable=varl1, width=20, show="*").grid(row=1, column=1)
tk.Entry(win1, textvariable=varl2, width=20, show="*").grid(row=2, column=1)
tk.Entry(win1, textvariable=varl3, width=20, show="*").grid(row=3, column=1)
# 在窗口上创建一个按钮
tk.Button(win1, command=button1, text="登录", relief="solid", width=15).grid(row=4, column=1)
# 进入事件循环
win1.mainloop()
