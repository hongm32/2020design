import os
import tkinter as tk
import tkinter.messagebox
import win32com.client


def Button1():
    ISBN = varl1.get()
    title = varl2.get()
    author = varl3.get()
    type = varl4.get()
    pub = varl5.get()
    count = varl6.get()

    if ISBN == "" or title == "":
        tkinter.messagebox.showerror("错误！", "ISBN和书名都需要进行填写！")
    else:
        sql = "INSERT INTO {} (ISBN,书名,作者,类型,出版时间,数量) VALUES ('{}','{}','{}','{}','{}',{})".format(
            tablename, ISBN, title, author, type, pub, count)
        conn.Execute(sql)  # 执行sql语句
        varl1.set("")
        varl2.set("")
        varl3.set("")
        varl4.set("")
        varl5.set("")
        varl6.set("")


mdb_file = "../【第37课】数据库的构建/图书借阅管理.mdb"  # 数据库文件
conn = win32com.client.Dispatch(r"ADODB.Connection")  # 建立连接对象
DSN = 'PROVIDER = Microsoft.ACE.OLEDB.12.0;DATA SOURCE = {}'.format(mdb_file)  # Access2007及以后
conn.Open(DSN)  # 用游标打开数据连接

tablename = 'books'

win = tk.Tk()
win.title("图书录入")
win.geometry('350x400')

varl1 = tk.StringVar()
varl2 = tk.StringVar()
varl3 = tk.StringVar()
varl4 = tk.StringVar()
varl5 = tk.StringVar()
varl6 = tk.StringVar()


# 在窗口上创建三个标签
tk.Label(win, text="ISBN", width=14).grid(row=1, column=0)
tk.Label(win, text="书名", width=14).grid(row=2, column=0)
tk.Label(win, text="作者", width=14).grid(row=3, column=0)
tk.Label(win, text="类型", width=14).grid(row=4, column=0)
tk.Label(win, text="出版时间", width=14).grid(row=5, column=0)
tk.Label(win, text="数量", width=14).grid(row=6, column=0)

tk.Entry(win, textvariable=varl1, width=30).grid(row=1, column=1)
tk.Entry(win, textvariable=varl2, width=30).grid(row=2, column=1)
tk.Entry(win, textvariable=varl3, width=30).grid(row=3, column=1)
tk.Entry(win, textvariable=varl4, width=30).grid(row=4, column=1)
tk.Entry(win, textvariable=varl5, width=30).grid(row=5, column=1)
tk.Entry(win, textvariable=varl6, width=30).grid(row=6, column=1)

# 在窗口上创建一个按钮
tk.Button(win, command=Button1, text="录入", relief="solid", width=15).grid(row=7, column=1)
# 进入事件循环
win.mainloop()

# 关闭数据库连接
conn.Close()
