import csv
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# 指定默认字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

# 读取数据
file = "A市公共自行车一月份运营数据.xlsx"
data = pd.read_excel(file)
data = data.dropna()  # 删除所有包含空值的行

# 自定义画布大小，单位英寸
plt.figure(figsize=(12, 12))

# A市自行车借还数量对比图
plt.subplot(3,  1,  1)  # 建立subplot网格，高为3，宽为1，激活第一个子图
plt.bar(data.index, data["借数量"], width=0.4, label="借数量")
plt.bar(data.index + 0.4, data["还数量"], width=0.4, label="还数量")
plt.xticks(data.index, data["投放站点编号"], rotation=270)  # 坐标轴标签替换，rotaion旋转
plt.legend(loc='best')  # 图例，best：自动选择最佳位置 upper center：上部居中等
plt.title('A市自行车借还数量对比图', size=20)
plt.gca().spines["right"].set_color("none")  # right边框属性设置为none不显示
plt.gca().spines["top"].set_color("none")  # top边框属性设置为none不显示

# A市自行车平均毎桩借还数图
data["每桩借车数"] = data["借数量"] / data["锁车桩数"]
data["每桩还车数"] = data["还数量"] / data["锁车桩数"]
plt.subplot(3,  1,  2)
plt.bar(data.index, data["每桩借车数"], label="平均每桩借车数")
plt.bar(data.index + 0.4, data["每桩还车数"], label="平均每桩还车数")
plt.plot(data.index + 0.2, -data["每桩借车数"])
plt.plot(data.index + 0.2, -data["每桩还车数"])
plt.xticks(data.index, data["投放站点编号"], rotation=270)  # 坐标轴标签替换，rotaion旋转
plt.legend(loc='best')  # 图例，best：自动选择最佳位置 upper center：上部居中等
plt.title('A市自行车平均毎桩借还数图', size=20)
plt.gca().spines["right"].set_color("none")  # right边框属性设置为none不显示
plt.gca().spines["top"].set_color("none")  # top边框属性设置为none不显示

# A市自行车还车数与维修量比图
data["修还比"] = data["维修数量"] / data["还数量"]
plt.subplot(3,  1,  3)
plt.bar(data.index, data["修还比"], label="维修数量与还车数量比")
plt.xticks(data.index, data["投放站点编号"], rotation=270)  # 坐标轴标签替换，rotaion旋转
plt.legend(loc='best')  # 图例，best：自动选择最佳位置 upper center：上部居中等
plt.title('A市自行车还车数与维修量比图', size=20)
plt.gca().spines["right"].set_color("none")  # right边框属性设置为none不显示
plt.gca().spines["top"].set_color("none")  # top边框属性设置为none不显示

plt.tight_layout()  # 调整子图间距
plt.savefig("A市自行车运营情况调查报告图表.png")
plt.show()
