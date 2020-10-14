from tkinter import *
import tkinter.ttk as ttk


root = Tk()
root.title("树结构")
root.resizable(0, 0)
tree = ttk.Treeview(root, height=20, show="tree")

# 读取文本文件数据
with open("行政区划.txt", 'r', encoding="UTF-8") as f:
    lines = f.readlines()

# 添加Treeview的数据项
for i in range(len(lines)):
    b = lines[i][:-1]
    if i == 0:
        exec(b + '=tree.insert("",' + str(i) + ',b,text=b)')
    elif "." not in b:
        exec(b + '=tree.insert(' + lines[0][:-1] + ',' + str(i) + ',b,text=b)')
    else:
        d = b.split('.')
        exec(d[1] + '=tree.insert(d[0],' + str(i) + ',d[1],text=d[1])')

# 添加垂直滚动条
yscrollbar = Scrollbar(root, orient=VERTICAL, command=tree.yview)
tree.configure(yscrollcommand=yscrollbar.set)
yscrollbar.pack(side=RIGHT, fill=Y)

tree.pack()
root.mainloop()
