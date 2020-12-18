import random


# 班级学生名单列表
class_list = [
    "01张晴晴", "02吴佳煜", "03钱秋萍", "04陆诗颖", "05邹佳芸", "06朱蒋岚", "07赵怡月", "08游欣悦",
    "09沈雨洋", "10徐佳雨", "11王欣怡", "12陈皖晴", "13朱辰媛", "14孙俏",   "15李宜霏", "16任煜霏",
    "17台育蕊", "18陈慧",   "19何雪",   "20莫佳妮", "21顾心怡", "22杨钰雯", "23苏雨欣", "24曾海瑞",
    "25张权凯", "26江宇轩", "27陈晨",   "28陈浩",   "29蒋熠晨", "30张思诚", "31罗一鸣", "32杨熠恒",
    "33周昊天", "34曹国梁", "35王奇",   "36沈心源", "37沈振亓", "38周顺利", "39康治坤", "40周杰",
    "41陆小凡", "42沈航宇", "43徐天成", "44鲍宇",   "45王缪丞", "46庞宇帆"
    ]


def luck1(_number):
    # 创建幸运儿空列表
    _luck = []
    for _ in range(_number):
        item = random.choice(class_list)
        _luck.append(item)
        class_list.remove(item)
    return _luck


def luck2(_number):
    _luck = []
    for _ in range(_number):
        idx = random.randint(0, len(class_list) - 1)
        item = class_list.pop(idx)
        _luck.append(item)
    return _luck


while True:
    bj_count = len(class_list)
    n = input("抽取几位({})：".format(bj_count))
    if n:
        n = int(n)
    else:
        n = 1
    if n <= 0 or bj_count == 0:
        break
    if len(class_list) < n:
        print("班级人数不足")
        continue
    luck_list = luck1(n)  # 每次抽取几位幸运儿
    # luck_list.sort()  # 排序
    print('幸运儿是：')
    for i in luck_list:  # 遍历输出幸运名单
        print('  ', i)
