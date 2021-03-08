import numpy as np  # 加载numpy模块并取名为np
import matplotlib
import matplotlib.pyplot as plt  # 加载matplotlib.pyplot并取名为plt


# 指定默认字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

x = np.arange(0, 2 * np.pi, 0.01)  # x在0到2π之间，每隔0.01取一个点
y1 = np.sin(x) 		               # 求sin(x)对应的列表y1的值
y2 = np.sin(-x)		               # 求sin(-x)对立的列表y2的值
y3 = np.sin(2 * x) / 2             # 求sin(2x)/2对应的列表y3的值

plt.plot(x, y1)		     # 绘制sin(x)的图像
plt.plot(x, y2)          # 绘制sin(-x)的图像
plt.plot(x, y3)          # 绘制sin(2x)/2的图像

plt.title('正弦函数图像', size=18)  # 设置图像标题
plt.xlabel('X')  # 设置X轴标题
plt.ylabel('Y')  # 设置Y轴标题
plt.show()  # 将绘制的函数图像窗口显示出来
