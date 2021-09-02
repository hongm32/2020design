# 百家姓
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
names_dict = dict([[i[0], i[1]] for i in names_dict.split("\n") if i])


def jiem(_text):
    _jie_text = ""
    for i in _text:
        _jie_text += names_dict.get(i, " ")
    return _jie_text


def jiam(_text):
    j_names_dict = dict(zip(names_dict.values(), names_dict.keys()))
    _jia_text = ""
    for i in _text:
        _jia_text += j_names_dict.get(i, random.choice("冲锋陷阵"))
    return _jia_text


text = "Be careful: There are five whistleblowers, David is one of them!"
text = 'hello'
jia_text = jiam(text)
jie_text = jiem(jia_text)
print("原文：", text)
print("密文：", jia_text)
print("解密：", jie_text)

input("运行结束，请按回车键退出...")
