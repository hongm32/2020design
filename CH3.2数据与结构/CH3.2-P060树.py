def out(t, s):  # 用递归算法输出树结构
    print('　' * s + t[0])  # 输出根,s控制根左边空格数
    s += 1
    for i in t[1:]:
        out(i, s)  # 递归输出子树


def ctree():  # 用列表生成树结构
    d = {}  # 定义字典d记录各节点的键与值
    f = open('树.txt', 'r')  # 打开文本文件备读
    x = f.readline()[0:-1]  # 读取首行，去掉末尾的换行符
    r = [x]  # 定义列表r存储树结构
    d.update({x: ''})  # 更新字典，加入根节点的键值对
    while 1:  # 永远循环
        x = f.readline()[0:-1]  # 读取文件的一行，去掉末尾的换行符
        if x == '':  # 内容为空，已到文尾
            break  # 退出循环
        y = x.split(',')  # 按逗号分割节点对
        for i in range(len(y)):  # 循环处理每对节点
            p = y[i].split('.')  # 按小数点分割节点为父节点与子节点
            obj = eval('r' + d[p[0]])  # 定位父节点
            obj.append([p[1]])  # 在列表r中父节点后追加子节点
            d.update({p[1]: d[p[0]] + '[' + str(i + 1) + ']'})  # 更新字典，加入子节点的键值对
    f.close()  # 关闭文件
    return r  # 返回结果列表r


tree = ctree()  # 调用函数ctree()生成树
out(tree, 0)  # 调用函数out()输出树
