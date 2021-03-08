import numpy as np  # 加载numpy模块并取名为np
import matplotlib.pyplot as plt  # 加载matplotlib.pyplot并取名为plt

x = np.arange(-10, 12, 0.01)   # x在-10到12之间，每隔0.01取一个点
y = x ** 2 - 2 * x + 1         # 通过解析式计算列表x对应的列表y的值


plt.plot(x, y)
plt.xlabel('X')  # 设置X轴标题
plt.ylabel('Y')  # 设置Y轴标题
plt.show()       # 将绘制的函数图像窗口显示出来
