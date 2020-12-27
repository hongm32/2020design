from tkinter import *
import tkinter.messagebox
import random
import datetime
import csv
import os


def get_grade(file):
    stu = [[] for _ in range(24)]  # 生成班级学号空列表
    stu_dict = {}  # 生成学生信息空字典
    # csv_file = '20021.csv'
    # CSV文件格式：班级，学号，姓名
    try:
        with open(file, encoding="GBK") as f:
            f_csv = csv.reader(f)
            for row in f_csv:
                if row[0].isdigit():
                    dm = row[0].zfill(2) + row[1].zfill(2)
                    stu[int(row[0]) - 1].append(dm)
                    stu_dict[dm] = row
    except UnicodeDecodeError:
        with open(file, encoding="UTF-8") as f:
            f_csv = csv.reader(f)
            for row in f_csv:
                if row[0].isdigit():
                    dm = row[0] + row[1]
                    stu[int(row[0]) - 1].append(dm)
                    stu_dict[dm] = row
    stu = [_item for _item in stu if len(_item) >= 10]
    return stu, stu_dict


def get_data(stu, stu_dict, _bj=0):
    data = []
    for index in stu[_bj]:
        if stu_dict[index][2]:
            data.append(index[-2:] + stu_dict[index][2])
    return data


def get_bj(v):  # 尺度（拉动条）激发班级
    global a
    global csv_file
    global bj
    global student, student_dict
    bj = v
    if not lb.curselection():
        csv_file = csv_files[0]
    else:
        csv_file = lb.get(lb.curselection())
    student, student_dict = get_grade(csv_file)
    a = get_data(student, student_dict, int(bj) - 1)
    reset()


def intomap():  # "下一个"按钮激发函数
    if lb.curselection() and csv_file != lb.get(lb.curselection()):
        get_bj(bj)
    if len(b) == 0:  # 如果点名完成一轮
        tkinter.messagebox.showwarning('随机点名器', '本轮点名完毕。\n要继续点名，请单击“重置”按钮。')
        return
    d1 = datetime.datetime.now()  # 记下开始时刻
    while True:
        i = random.randint(0, len(b) - 1)  # 产生随机整数
        var.set(b[i])
        entry.update()  # 刷新显示姓名
        d2 = datetime.datetime.now()  # 记下当前时刻
        d = d2 - d1
        if d.seconds > 0 or len(b) == 1:  # 时差达到1秒
            break
    i = random.randint(0, len(b) - 1)
    var.set(b.pop(i))  # 列表b中删除该姓名
    var1.set("[进度]" + str(len(a) - len(b)) + "/" + str(len(a)))


def reset():  # "重置"按钮激发函数
    global b
    b = []
    for i in a:  # 从列表a中读取全部姓名到b
        b.append(i)
    var1.set("[进度]" + str(len(a) - len(b)) + "/" + str(len(a)))


def scan_files(directory, prefix=None, postfix=None):
    files_list = []
    for special_file in os.listdir(directory):
        file_path = os.path.join(directory, special_file)
        if not os.path.isdir(file_path):
            if postfix:
                if special_file.endswith(postfix):
                    files_list.append(special_file)
            elif prefix:
                if special_file.startswith(prefix):
                    files_list.append(special_file)
            else:
                files_list.append(special_file)
    return files_list


# 获取所有年级数据文件列表
csv_files = scan_files(".", postfix='.csv')
root = Tk()  # 创建主窗口
root.title("随机点名器")  # 设置窗口标题
root.geometry('840x350+300+200')  # 设置窗口大小及位置
root.resizable(0, 0)  # 禁止调整窗口大小
var = StringVar()  # 定义StringVar()类型
var1 = StringVar()
b = []  # b作为列表a的备份
bj = 1
csv_file = None
student, student_dict = get_grade(csv_files[-1])
a = get_data(student, student_dict, 0)
# 在窗口上建1个Listbox
lb = Listbox(root, height=3, selectmode=SINGLE)
lb.grid(row=0, column=0, padx=20)
for item in csv_files:
    lb.insert(END, item)
lb.selection_set(len(csv_files)-1)
# 在窗口上建1个Scale
scale = Scale(root, label=None, from_=1, to=len(student), orient=HORIZONTAL, length=600, showvalue=1,
              tickinterval=1, resolution=1, command=get_bj)
scale.grid(row=0, column=1, padx=20, columnspan=3)
label = Label(root, bg='green', fg='white', width=20, text='班级')
# label.grid(row=0, column=3, columnspan=1)
# 在窗口上建1个Entry
entry = Entry(root, textvariable=var, font=('黑体', 150), width=8, justify=CENTER)
entry.grid(row=1, column=0, columnspan=4, padx=20, sticky=NS)
# 在窗口上建1个Button
button = Button(root, text="下一个", command=intomap, relief="solid", width=28, font=('黑体', 14))
button.grid(row=2, column=0, pady=20, columnspan=2)
# 在窗口上建1个Entry
entry2 = Entry(root, textvariable=var1, font=('黑体', 16), width=11, bg='blue', fg='white', justify=CENTER)
entry2.grid(row=2, column=2)
# 在窗口上建1个Button
button2 = Button(root, text="重置", command=reset, relief="solid", width=6, font=('宋体', 10))
button2.grid(row=2, column=3)

reset()
root.mainloop()  # 进入事件（消息）循环
