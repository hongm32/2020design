# 公交线路客流量图

import matplotlib
import matplotlib.pyplot as plt
import csv


# 指定默认字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

# 读取数据
t = []
b27 = []
b49 = []
file = "27路和49路公交线路客流量表.csv"
with open(file, encoding="GBK") as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        if row[0].isdigit():
            t.append(row[0])
            b27.append(int(row[1]))
            b49.append(int(row[2]))

# 图表
plt.figure()
plt.plot(t, b27, linewidth='1', label="小明乘坐线路(27路)", marker='o')
plt.plot(t, b49, linewidth='1', label="妈妈乘坐线路(49路)", marker='o', markersize=6)
plt.legend(loc='best')  # 图例，best：自动选择最佳位置 upper center：上部居中等
plt.title('公交线路客流量', size=20)
plt.xlabel("时间段", size=12)
plt.ylabel("客流量", size=12)
plt.show()
