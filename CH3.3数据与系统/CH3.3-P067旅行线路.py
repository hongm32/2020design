from tkinter import *  # 导入tkinter模块
import tkinter.messagebox  # 弹窗库


root = Tk()  # 创建一个窗口
root.title("线路操作")  # 设置窗口标题
root.geometry('580x220')  # 设置窗口大小
root.resizable(0, 0)  # 禁止调整窗口大小
var = StringVar()  # 定义StringVar()类型


def intomap():  # Button按钮"添加线路"激发函数
    if var.get().strip() == "":
        tkinter.messagebox.showerror('错误', '输入内容不能为空！')
    else:
        with open("旅行线路.txt", 'a+', encoding="UTF-8") as c:  # 以追加模式打开文件
            c.write(var.get() + "\n")  # 在文件末尾添加text里的内容
        tkinter.messagebox.showinfo('提示', '录入成功！')
    var.set("")  # 清除录入内容以免重复录入
    entry.focus_set()  # 输入框获得焦点


def query():  # Button按钮"查询线路"激发函数
    with open("旅行线路.txt", 'r', encoding="UTF-8") as c:  # 以只读模式打开文件
        lines = c.readlines()  # 读取文件全部内容
    text.delete('0.0', 'end')  # 清空文本框内容
    for i in lines:
        text.insert(INSERT, i)  # INSERT表示输入光标所在的位置


# 在窗口上建一个文本标签
Label(root, text='请输入线路', font=('Arial', 10)).pack()
# 在窗口上建一个输入框
entry = Entry(root, textvariable=var, width=82)
entry.pack()
# 在窗口上建一个Button按钮
Button(root, text="添加线路", command=intomap, relief="solid", width=10).pack()
# 在窗口上建一个Button按钮
Button(root, text="查询线路", command=query, relief="solid", width=10).pack()
# 在窗口上建一个文本框
text = Text(root, width=82, height=8)  # 82个字符（每个汉字算2个字符）的宽度，8行
text.pack()
entry.focus_set()  # 输入框获得焦点
root.mainloop()  # 进入事件（消息）循环
