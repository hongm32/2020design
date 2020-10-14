#!/usr/bin/python3
# coding:utf-8
"""
简介：本脚本用于计算24点
作者：学虹夜雨
"""


def _cal(a, b):
    temp = {'+': a + b, '-': a - b, '--': b - a, '*': a * b}
    if b != 0 and a != 0:
        temp['/'] = float(a) / b
        temp['\\'] = float(b) / a
    return temp


def cal(num, disp=1):
    for i0 in num:
        for i1 in num:
            if i1 == i0:
                continue
            else:
                for i2 in num:
                    if i2 == i1 or i2 == i0:
                        continue
                    else:
                        for i3 in num:
                            if i3 == i1 or i3 == i0 or i3 == i2:
                                continue
                            else:
                                temp1 = _cal(num[i0], num[i1])
                                for k1 in temp1:
                                    temp2 = _cal(temp1[k1], num[i2])
                                    for k2 in temp2:
                                        temp3 = _cal(temp2[k2], num[i3])
                                        for k3 in temp3:
                                            if temp3[k3] == 24:
                                                if disp == 1:
                                                    print('(({}{}{}){}{}){}{}=24'.format(
                                                        num[i0], k1, num[i1], k2, num[i2], k3, num[i3]))
                                                return True


def get_none():
    # 查看所有的无解组，共176
    max_number = 11
    fail = 0
    failist = []
    for i1 in range(1, max_number):
        for i2 in range(1, max_number):
            for i3 in range(1, max_number):
                for i4 in range(1, max_number):
                    num = {1: i1, 2: i2, 3: i3, 4: i4}
                    if not cal(num, 0):
                        temp = [num[1], num[2], num[3], num[4]]
                        temp.sort()
                        if temp not in failist:
                            failist.append(temp)
                            fail = fail + 1
    print(failist)
    print('总数:{},无解:{}'.format(max_number**4, fail))


# 单独测试一组
test = [1, 5, 5, 5]
num_dict = {1: test[0], 2: test[1], 3: test[2], 4: test[3]}
cal(num_dict)
# get_none()
