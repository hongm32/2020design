import win32com.client
import os
import tkinter as tk
import tkinter.messagebox


def button1():
    global password1, name1

    name1 = var11.get()
    password1 = var12.get()
    sql1 = "SELECT * FROM {} WHERE {}='{}'".format(table, name, name1)
    rs.Open(sql1, conn, 1, 1)
    if rs.RecordCount:
        while not rs.EOF:
            if password1 == rs.Fields(1).Value:
                is_login = 1  # 登陆成功
                break
            rs.MoveNext()
        else:
            tkinter.messagebox.showerror("错误", "密码输入错误，请重新输入！")
    else:
        tkinter.messagebox.showerror("错误", "没有该用户名！")


def button2():
    password21 = var21.get()
    password22 = var22.get()
    password23 = var23.get()
    if password1 == password21 and password22 == password23 and password1 != password23:
        sql2 = "UPDATE "
        conn.Execute(sql2)


mdb_file = "图书借阅管理.mdb"  # 数据库文件
conn = win32com.client.Dispatch(r"ADODB.Connection")  # 建立连接对象
DSN = 'PROVIDER = Microsoft.ACE.OLEDB.12.0;DATA SOURCE = {}'.format(mdb_file)  # Access2007及以后
conn.Open(DSN)  # 用游标打开数据连接

# 打开一个记录集Recordset
rs = win32com.client.Dispatch(r'ADODB.Recordset')

