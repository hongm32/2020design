def out(t, s):
    print(' ' * s + t[0] + ":" + str(v[t[0]]))
    s += 1
    for item in t[1:]:
        out(item, s)


def ctree():
    global d, v
    f = open('CH3.2-P064最短时间分析树.txt', 'r')
    x = f.readline()[0:-1]
    t = x.find(':')
    r = [x[:t]]
    d.update({x[:t]: ''})
    v.update({x[:t]: [eval(x[t + 1:]), 1]})
    while True:
        x = f.readline()[0:-1]
        if x == '':
            break
        y = x.split(',')
        for item in range(len(y)):
            t = y[item].find(':')
            y1 = y[item][:t]
            y2 = eval(y[item][t + 1:])
            p = y1.split('.')
            obje = eval('r' + d[p[0]])
            obje.append([p[1]])
            d.update({p[1]: d[p[0]] + '[' + str(item + 1) + ']'})
            v.update({p[1]: [v[p[0]][0] + y2, 0]})
            v.update({p[0]: [v[p[0]][0], 1]})
    f.close()
    return r


d = {}
v = {}
min_value = 999
minv = 0
tree = ctree()
out(tree, 0)
for i in v:
    if v[i][1] == 0 and v[i][0] < min_value:
        min_value = v[i][0]
        minv = i
print("最短时间:", min_value)
print("最短时间的一条路径:", end=' ')
print(tree[0], end=' ')
w = d[minv]
g = w.find(']')
while g > 0:
    obj = eval('tree' + w[:g + 1] + '[0]')
    print('-', obj, end=' ')
    g = w.find(']', g + 1)
print()
