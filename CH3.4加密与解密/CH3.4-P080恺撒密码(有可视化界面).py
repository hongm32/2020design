from tkinter import *       # 导入tkinter模块
root = Tk()                 # 建立一个窗口
root.title("恺撒加密")      # 设置窗口标题
root.geometry('300x200')    # 设置窗口大小


def caesar_cipher():  # “加密”按钮激发函数
    c = mingwen.get("0.0", "end")   # 获取mingwen对象的内容（明文）
    b = ""
    miwen.delete("0.0", "end")    # 清空miwen对象的内容
    for i in range(len(c)):       # 获取明文内容的每一个字符，并加密
        if 'a' <= c[i] <= 'w' or 'A' <= c[i] <= 'W':   # 判断a～w或A～W间的字母
            b = b + chr(ord(c[i]) + 3)               # 生成密文
        elif 'x' <= c[i] <= 'z' or 'X' <= c[i] <= 'Z':  # 判断x～z或X～Z间的字母
            b = b + chr(ord(c[i]) - 23)              # 生成密文
        else:
            b = b + c[i]                           # 字母以外的明文不变
    miwen.insert("0.0", b)                      # 在miwen对象中显示结果


Label(root, text='请输入明文', font=('Arial', 10)).pack()
mingwen = Text(root, width=300, height=4)
mingwen.pack()
mingwen.focus_set()    # 获得焦点
Button(root, text="加密", command=caesar_cipher, relief="solid", width=10).pack()
Label(root, text='恺撒密文', font=('Arial', 10)).pack()
miwen = Text(root, width=300, height=4)
miwen.pack()
root.mainloop()
