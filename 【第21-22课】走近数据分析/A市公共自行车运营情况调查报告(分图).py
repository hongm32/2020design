import csv
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


# 指定默认字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

# 读取数据
data = [[] for _ in range(8)]
file = "A市公共自行车一月份运营数据.csv"
with open(file, encoding="GBK") as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        if "GXZX" in row[0]:
            for idx, value in enumerate(row):
                if idx == 0:
                    data[idx].append(value)
                else:
                    data[idx].append(int(value))
            data[5].append(int(data[2][-1] / data[1][-1]))
            data[6].append(int(data[3][-1] / data[1][-1]))
            data[7].append(round(data[4][-1] / data[3][-1] * 100, 1))
    for i in range(1, 8):
        data[i] = np.asarray(data[i])
    data.append(np.arange(len(data[0])))
#  print(data)

# A市自行车借还数量对比图
plt.figure(figsize=(12, 6))
plt.bar(data[-1], data[2], width=0.4, label="借数量")
plt.bar(data[-1] + 0.4, data[3], width=0.4, label="还数量")
plt.xticks(data[-1], data[0], rotation=270)  # 坐标轴标签替换，rotaion旋转
plt.legend(loc='best')  # 图例，best：自动选择最佳位置 upper center：上部居中等
plt.title('A市自行车借还数量对比图', size=20)
plt.savefig("A市自行车运营情况调查报告图表_借还对比.png")
plt.show()

# A市自行车平均毎桩借还数图
plt.figure(figsize=(12, 6))
plt.bar(data[-1], data[5], width=0.4, label="平均每桩借车数")
plt.bar(data[-1] + 0.4, data[6], width=0.4, label="平均每桩还车数")
plt.plot(data[-1] + 0.2, -data[5])
plt.plot(data[-1] + 0.2, -data[6])
plt.xticks(data[-1], data[0], rotation=270)  # 坐标轴标签替换，rotaion旋转
plt.legend(loc='best')  # 图例，best：自动选择最佳位置 upper center：上部居中等
plt.title('A市自行车平均毎桩借还数图', size=20)
plt.savefig("A市自行车运营情况调查报告图表_每桩借还.png")
plt.show()

# A市自行车还车数与维修量比图
plt.figure(figsize=(12, 6))
plt.bar(data[-1], data[7], label="维修数量与还车数量比")
plt.xticks(data[-1], data[0], rotation=270)  # 坐标轴标签替换，rotaion旋转
plt.legend(loc='best')  # 图例，best：自动选择最佳位置 upper center：上部居中等
plt.title('A市自行车还车数与维修量比图', size=20)
plt.savefig("A市自行车运营情况调查报告图表_修还比值.png")
plt.show()
