from tkinter import *
from tkinter import ttk
import tkinter.messagebox           # 弹窗库
import win32com.client   # 先要安装与Python匹配的pywin32


def CmdChk():
    global tree, vbar, TblName, FstFldName, CrRecFstVolVal, fieldsname
    if v.get() == 0:
        tkinter.messagebox.showinfo('图书信息管理系统','请先选择数据表名。')
        return 0
    tree.destroy()
    vbar.destroy()
    conn.Open(DSN)
    CrRecFstVolVal = []
    if v.get() == 1:
        TblName = 'book'
    elif v.get() == 2:
        TblName = 'borrow'
    elif v.get() == 3:
        TblName = 'student'
    rs = win32com.client.Dispatch(r'ADODB.Recordset')
    rs.Open('[' + TblName + ']', conn, 1, 3)
    var.set("当前数据表名：" + TblName + "[记录数:" + str(rs.RecordCount) + "]")
    FstFldName = rs.Fields[0].Name
    fieldsname = []
    for i in range(rs.Fields.Count):
        fieldsname.append(rs.Fields[i].Name)
    bookList = []
    count = 0
    while not rs.EOF:
        t='('
        for i in range(rs.Fields.Count):
            t = t + '"' + str(rs.Fields[i].Value) + '",'
        t = t[:-1] + ')'
        bookList.append(eval(t))
        count += 1
        rs.MoveNext()
    conn.Close()
    
    tree = ttk.Treeview(frame0, columns=fieldsname, show='headings', height=10)
    for i in range(len(fieldsname)):
        if fieldsname[i] in ["ISBN", "书名"]:
            tree.column(fieldsname[i], width=150, anchor='center')
        elif fieldsname[i] in ["编号", "学号", "类型"]:
            tree.column(fieldsname[i], width=40, anchor='center')
        else:
            tree.column(fieldsname[i], width=80, anchor='center')
    for i in range(len(fieldsname)):
        tree.heading(fieldsname[i], text=fieldsname[i])
    for item in bookList:
        tree.insert('', 'end', values=item)
    tree.grid(row=4, column=0, columnspan=10, sticky=W)
    tree.bind('<ButtonRelease-1>', treeviewClick)  #绑定单击释放事件

    #垂直滚动条
    vbar = Scrollbar(frame0, orient=VERTICAL, command=tree.yview)
    tree.configure(yscrollcommand=vbar.set)
    tree.grid(row=0, column=0, sticky=NSEW)
    vbar.grid(row=0, column=10, padx=0, sticky=NS)
 

def CmdAdd():         # 增加记录
    global tree, va0, va1, va2, va3, va4, va5, top, e1, AddMdf, root
    if v.get() == 0:    # 如果没有选中数据表
        tkinter.messagebox.showinfo('图书信息管理系统', '请先选择数据表名。')
        return
    AddMdf = 0          # 0：增加记录，1：修改记录
    # root.withdraw()   # 隐藏窗体,防止交叉操作
    root.state("withdrawn")
    top = Toplevel(root)
    top.title("增加记录[" + TblName + "]")
    size = '%dx%d+%d+%d' % (330, len(fieldsname) * 36, root.winfo_screenwidth() / 2 - 440, root.winfo_screenheight() / 2 - 310)
    top.geometry(size)                 # 设置窗口大小和位置
    top.resizable(0, 0)                # 禁止调整窗口大小
    top.attributes("-topmost", 1)      # 窗口置顶

    lbl1 = []
    e1 = []
    v1 = []
    for i in range(len(fieldsname)):
        lbl1.append(Label(top, text=fieldsname[i]))
        exec("e1.append(Entry(top,textvariable=va" + str(i) + ",width=25))")
        exec("va" + str(i) + ".set('')")   #清空内容
        exec("lbl1[i].grid(row=" + str(i) + ",column=0,padx=2,sticky=E)")
        exec("e1[i].grid(row=" + str(i) + ",column=1,padx=2,pady=4)")
    Button(top, text='提交', width=10, command=CmdSubmit).grid(row=len(fieldsname) + 1, column=1, padx=10, pady=10)
    Button(top, text='取消', width=10, command=CmdCancel).grid(row=len(fieldsname) + 1, column=0, padx=10, pady=10)
    top.protocol("WM_DELETE_WINDOW", callback)
    top.focus_set()
    e1[0].focus_set()


def callback0():
    if tkinter.messagebox.askokcancel("图书信息管理系统", "真心要退出？"):
        root.destroy()


def callback():
    msgtitle="增加记录" if AddMdf == 0 else "修改记录"
    if tkinter.messagebox.askokcancel(msgtitle, "数据未提交，真心要退出？"):
        top.destroy()
        root.deiconify()      # 显示窗体
        # root.state("normal")   # 显示窗体
    else:
        top.focus_set()
        e1[0].focus_set()


def CmdSubmit():   # 提交
    vals = []
    for i in range(len(fieldsname)):
        if eval("va" + str(i) + ".get()").strip() == '':
            tkinter.messagebox.showwarning('图书信息管理系统', '[' + fieldsname[i] + ']不能为空。')
            e1[i].focus_set()
            return
        exec("vals.append(va" + str(i) + ".get())")
    conn.Open(DSN)
    if AddMdf == 0:    # 增加记录
        sql = "Insert Into " + TblName + " " +str(tuple(fieldsname)).replace("'","") + " Values " + str(tuple(vals))
    else:            #修改记录
        sql = "Update " + TblName + " Set "
        for i in range(len(fieldsname)):
            sql = sql + fieldsname[i] + "='" + vals[i] + "',"
        sql = sql[:-1] + " where " + fieldsname[0] + "='" + rec1val[0] + "'"
    conn.Execute(sql)  # 执行sql语句
    conn.Close()
    top.destroy()
    root.deiconify()   # 显示窗体
    CmdChk()


def CmdCancel():       # 取消
    vals = []
    for i in range(len(fieldsname)):
        exec("vals.append(va" + str(i) + ".get())")
    if '' in vals:          # 有值为空
        top.destroy()
        # root.deiconify()   # 显示窗体
        root.state("normal")
    else:
        callback()
       
    
def CmdDel():      # 删除记录（可以同时选中多行同时删除）
    global CrRecFstVolVal
    if v.get() == 0:   # 如果没有选中数据表
        tkinter.messagebox.showinfo('图书信息管理系统', '请先选择数据表名。')
        return
    if CrRecFstVolVal == []:   # 如果没有选中记录
        tkinter.messagebox.showinfo('图书信息管理系统', '请单击要删除的记录。')
        return
    if tkinter.messagebox.askokcancel('图书信息管理系统', '确实要删除“' + TblName + '”中' + FstFldName + '为' + str(CrRecFstVolVal) + '的记录吗？\n危险！此操作不可恢复！'):
        conn.Open(DSN)
        sql = "Delete * FROM " + TblName + " where "
        sql = sql + FstFldName + " = '" + str(CrRecFstVolVal[0]) + "'"
        if len(CrRecFstVolVal) > 1:
          for i in range(1, len(CrRecFstVolVal)):
            sql = sql + ' or '+ FstFldName + " = '" + str(CrRecFstVolVal[i]) + "'"
        conn.Execute(sql)  # 执行sql语句
        conn.Close()
        CmdChk()


def CmdMdf():      # 修改记录
    if v.get() == 0:
        tkinter.messagebox.showinfo('图书信息管理系统', '请先选择数据表名。')
        return
    if CrRecFstVolVal == []:   # 如果没有选中记录
        tkinter.messagebox.showinfo('图书信息管理系统', '请单击要修改的记录。')
        return
    global tree, va0, va1, va2, va3, va4, va5, va5, va6, va7, top, e1, rec1val, AddMdf
    AddMdf = 1
    root.withdraw()   # 隐藏窗体,防止交叉操作
    top=Toplevel(root)
    top.title("修改记录[" + TblName + "]")
    size = '%dx%d+%d+%d' % (330, 230, root.winfo_screenwidth() / 2 - 440, root.winfo_screenheight() / 2 - 310)
    top.geometry(size)                 # 设置窗口大小和位置
    top.resizable(0, 0)                 # 禁止调整窗口大小
    top.attributes("-topmost", 1)      # 窗口置顶

    lbl1 = []
    e1 = []
    v1 = []
    for i in range(len(fieldsname)):
        lbl1.append(Label(top, text=fieldsname[i]))
        exec("e1.append(Entry(top,textvariable=va" + str(i) + ",width=25))")
        exec("va" + str(i) + ".set('" + rec1val[i] + "')")   # 取得初始内容
        exec("lbl1[i].grid(row=" + str(i) + ",column=0,padx=2,sticky=E)")
        exec("e1[i].grid(row=" + str(i) + ",column=1,padx=2,pady=4)")
    Button(top, text='提交', width=10, command=CmdSubmit).grid(row=len(fieldsname) + 1, column=1, padx=10, pady=10)
    Button(top, text='取消', width=10, command=CmdCancel).grid(row=len(fieldsname) + 1, column=0, padx=10, pady=10)
    top.protocol("WM_DELETE_WINDOW", callback)
    top.focus_set()
    e1[0].focus_set()


def CmdQry():
    tkinter.messagebox.showinfo('图书信息管理系统', '“查询”功能期待你的加盟哦~~')


def CmdGrp():
    tkinter.messagebox.showinfo('图书信息管理系统', '“备用”功能期待你的加盟哦~~')


def treeviewClick(event):  # 单击
    global CrRecFstVolVal, rec1val
    CrRecFstVolVal = []
    rec1val = ()
    for item in tree.selection():
        if len(rec1val) == 0:
            rec1val=tree.item(item, "values")
        item_text = tree.item(item, "values")
        CrRecFstVolVal.append(item_text[0])


conn = win32com.client.Dispatch(r"ADODB.Connection")
# DSN = 'PROVIDER = Microsoft.Jet.OLEDB.4.0;DATA SOURCE = 图书借阅管理.mdb'  # Access2003及以前
DSN = 'PROVIDER = Microsoft.ACE.OLEDB.12.0;DATA SOURCE = 图书借阅管理.mdb'  # Access2007及以后

root = Tk()
root.title("图书信息管理系统")
size = '%dx%d+%d+%d' % (680, 340, root.winfo_screenwidth() / 2 - 440, root.winfo_screenheight() / 2 - 310)
root.geometry(size)                 # 设置窗口大小
root.resizable(0, 0)                 # 禁止调整窗口大小
var = StringVar()
TblName = ''
fieldsname = []
CrRecFstVolVal = []
FstFldName = ''
v = IntVar()
v.set(0)
va0 = StringVar()
va1 = StringVar()
va2 = StringVar()
va3 = StringVar()
va4 = StringVar()
va5 = StringVar()
va6 = StringVar()
va7 = StringVar()
top = ''
e1 = []
rec1val = ()
AddMdf = 0

# 在窗口上建3个Radiobutton单选钮
rb1 = Radiobutton(root, text='图书信息管理', command=CmdChk, variable=v, value=1)
rb1.grid(row=0, column=0)
rb2 = Radiobutton(root, text='图书借阅管理', command=CmdChk, variable=v, value=2)
rb2.grid(row=0, column=1)
rb3 = Radiobutton(root, text='学生信息管理', command=CmdChk, variable=v, value=3)
rb3.grid(row=0, column=2)

# 在窗口上建5个Button按钮
Cmd1 = Button(root, text="增加", command=CmdAdd, relief="solid", width=10)
Cmd1.grid(row=1,column=0)
Cmd2 = Button(root, text="修改", command=CmdMdf, relief="solid", width=10)
Cmd2.grid(row=1, column=1)
Cmd3=Button(root, text="删除", command=CmdDel, relief="solid", width=10)
Cmd3.grid(row=1, column=2, padx=10)
Cmd4=Button(root, text="查询", command=CmdQry, relief="solid", width=10)
Cmd4.grid(row=1, column=3, padx=10)
Cmd5=Button(root, text="备用", command=CmdGrp, relief="solid", width=10)
Cmd5.grid(row=1, column=4, padx=10)

# 在窗口上建一个输入框，一个框架，框架里建Treeview和Scrollbar
entry = Entry(root, textvariable=var, state='readonly', width=98)
entry.grid(row=2, column=0, columnspan=10, sticky=W)
frame0 = ttk.Frame(root)
tree = ttk.Treeview(frame0)
vbar = ttk.Scrollbar(frame0)
frame0.grid(row=3, column=0, columnspan=6, sticky=W)
root.protocol("WM_DELETE_WINDOW", callback0)
root.attributes("-topmost", 1)      # 窗口置顶
root.mainloop()
