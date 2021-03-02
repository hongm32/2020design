import tkinter
import random

names_dict = """
赵0
钱1
孙2
李3
周4
吴5
郑6
王7
冯8
陈9
褚a
卫b
蒋c
沈d
韩e
杨f
朱g
秦h
尤i
许j
何k
吕l
施m
张n
孔o
曹p
严q
华r
金s
魏t
陶u
姜v
戚w
谢x
邹y
喻z
福A
水B
窦C
章D
云E
苏F
潘G
葛H
奚I
范J
彭K
郎L
鲁M
韦N
昌O
马P
苗Q
凤R
花S
方T
俞U
任V
袁W
柳X
唐Y
罗Z
薛.
伍-
余_
米+
贝=
姚/
孟?
顾#
尹%
江&
钟*
费,
计!
龚:
"""
names_dict = dict([i for i in names_dict.split("\n") if i])
j_names_dict = dict(zip(names_dict.values(), names_dict.keys()))


def jiem():
    _text = miwen.get('0.0', 'end')[:-1]
    _jie_text = ""
    mingwen2.config(state="normal")
    mingwen2.delete('0.0', 'end')
    for i in _text:
        _jie_text += names_dict.get(i, " ")
    mingwen2.insert('0.0', _jie_text)
    mingwen2.config(state="disabled")


def jiam():
    _text = mingwen.get("0.0", "end")[:-1]
    _jia_text = ""
    miwen.delete('0.0', 'end')
    for i in _text:
        _jia_text += j_names_dict.get(i, random.choice("冲锋陷阵"))
    miwen.insert("0.0", _jia_text)
    # miwen.config(state="disabled")


root = tkinter.Tk()
root.title("百家姓")
root.geometry('300x300')
tkinter.Label(root, text='请输入明文', font=('楷体', 10)).pack()
mingwen = tkinter.Text(root, width=300, height=4)
mingwen.pack()
mingwen.focus_set()
tkinter.Button(root, text="加密", command=jiam, relief="solid", width=10).pack()
tkinter.Label(root, text='百家姓密文', font=('楷体', 10)).pack()
miwen = tkinter.Text(root, width=300, height=4)
miwen.pack()
tkinter.Button(root, text='解密', command=jiem, relief='solid', width=10).pack()
tkinter.Label(root, text='解密得到的明文', font=('楷体', 10)).pack()
mingwen2 = tkinter.Text(root, width=300, height=4, state="disabled")
mingwen2.pack()
root.mainloop()
