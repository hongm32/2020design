import os
import tkinter as tk
import tkinter.messagebox
import win32com.client


def Button1():
    name = var1.get()
    passwd = var2.get()
    sql = "SELECT 学号,密码 FROM student WHERE 学号='{}'".format(name)
    rs.Open(sql, conn, 1, 1)
    if rs.RecordCount:
        while not rs.EOF:
            if passwd == rs.Fields(1).Value:
                tkinter.messagebox.showinfo("正确", "密码输入正确！")
                win.destroy()
                break
            rs.MoveNext()
        else:
            tkinter.messagebox.showerror("错误", "密码输入错误，请重新输入！")
    else:
        tkinter.messagebox.showerror("错误", "没有该用户名！")


mdb_file = "../【第37课】数据库的构建/图书借阅管理.mdb"  # 数据库文件
conn = win32com.client.Dispatch(r"ADODB.Connection")  # 建立连接对象
DSN = 'PROVIDER = Microsoft.ACE.OLEDB.12.0;DATA SOURCE = {}'.format(mdb_file)  # Access2007及以后
conn.Open(DSN)  # 用游标打开数据连接

# 打开一个记录集Recordset
rs = win32com.client.Dispatch(r'ADODB.Recordset')
TABLE = "student"

win = tk.Tk()
win.title("登录界面")
win.geometry('350x400')
win.resizable(0, 0)  # 禁止调整窗口大小
var1 = tk.StringVar()
var2 = tk.StringVar()

# 在窗口上创建标签
tk.Label(win, text="学号", width=5).grid(row=1, column=0)
tk.Label(win, text="密码", width=5).grid(row=2, column=0)
# 在窗口上创建输入框
tk.Entry(win, textvariable=var1, width=30).grid(row=1, column=1)
tk.Entry(win, textvariable=var2, width=30).grid(row=2, column=1)
# 在窗口上创建一个按钮
tk.Button(win, command=Button1, text="登录", relief="solid", width=15).grid(row=3, column=1)

# 进入事件循环
win.mainloop()

# 关闭数据库连接
conn.Close()
