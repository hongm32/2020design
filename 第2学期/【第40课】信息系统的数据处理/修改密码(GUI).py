import win32com.client
import os
import tkinter as tk
import tkinter.messagebox


def Button1():
    global password, name

    name = var11.get()
    password = var12.get()
    sql1 = """SELECT 
                  * 
                  FROM {} 
                  WHERE {}='{}'""".format(Table, Name, name)
    rs.Open(sql1, conn, 1, 1)
    if rs.RecordCount:
        while not rs.EOF:
            if password == rs.Fields(1).Value:
                win1.destroy()
                windows2()
                break
            rs.MoveNext()
        else:
            tkinter.messagebox.showerror("错误", "密码输入错误，请重新输入！")
    else:
        tkinter.messagebox.showerror("错误", "没有该用户名！")


def Button2():
    password21 = var21.get()
    password22 = var22.get()
    password23 = var23.get()
    if password == password21 and password22 == password23 and password != password23:
        sql2 = """UPDATE {} 
                      SET {}='{}' 
                      WHERE {}='{}'""".format(Table, Password, password23, Name, name)
        conn.Execute(sql2)
        tkinter.messagebox.showinfo("正确", "密码修改成功！")
        win2.destroy()
    else:
        # 进入事件循环
        win2.mainloop()


def windows1():
    global win1, var11, var12

    win1 = tk.Tk()
    win1.title("登陆界面")
    win1.geometry('350x400')
    win1.resizable(0, 0)  # 禁止调整窗口大小
    var11 = tk.StringVar()
    var12 = tk.StringVar()

    # 在窗口上创建标签
    tk.Label(win1, text="学号", width=5).grid(row=1, column=0)
    tk.Label(win1, text="密码", width=5).grid(row=2, column=0)
    # 在窗口上创建输入框
    tk.Entry(win1, textvariable=var11, width=30).grid(row=1, column=1)
    tk.Entry(win1, textvariable=var12, width=30, show="*").grid(row=2, column=1)
    # 在窗口上创建一个按钮
    tk.Button(win1, command=Button1, text="登陆", relief="solid", width=15).grid(row=3, column=1)

    # 进入事件循环
    win1.mainloop()


def windows2():
    global win2, var21, var22, var23

    win2 = tk.Tk()
    win2.title("密码修改")
    win2.geometry('350x400')
    win2.resizable(0, 0)  # 禁止调整窗口大小
    var21 = tk.StringVar()
    var22 = tk.StringVar()
    var23 = tk.StringVar()

    # 在窗口上创建标签
    tk.Label(win2, text="原密码", width=10).grid(row=1, column=0)
    tk.Label(win2, text="新密码", width=10).grid(row=2, column=0)
    tk.Label(win2, text="再输一次密码", width=10).grid(row=3, column=0)
    # 在窗口上创建输入框
    tk.Entry(win2, textvariable=var21, width=30, show="*").grid(row=1, column=1)
    tk.Entry(win2, textvariable=var22, width=30, show="*").grid(row=2, column=1)
    tk.Entry(win2, textvariable=var23, width=30, show="*").grid(row=3, column=1)
    # 在窗口上创建一个按钮
    tk.Button(win2, command=Button2, text="确定", relief="solid", width=15).grid(row=4, column=1)


mdb_file = "../【第37课】数据库的构建/图书借阅管理.mdb"  # 数据库文件
conn = win32com.client.Dispatch(r"ADODB.Connection")  # 建立连接对象
DSN = 'PROVIDER = Microsoft.ACE.OLEDB.12.0;DATA SOURCE = {}'.format(mdb_file)  # Access2007及以后
conn.Open(DSN)  # 用游标打开数据连接

# 打开一个记录集Recordset
rs = win32com.client.Dispatch(r'ADODB.Recordset')

Table = 'student'
Name = "学号"
Password = "密码"
windows1()

# 关闭数据库连接
conn.Close()
