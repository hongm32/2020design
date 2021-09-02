import numpy as np  # 加载numpy模块并取名为np
import matplotlib.pyplot as plt  # 加载matplotlib.pyplot并取名为plt


x = np.arange(-1.5, 2.5, 0.1)  # x在-1.5到2.5之间，每隔0.1取一个点
y = x ** 3 - x ** 2 - x - 1
plt.plot(x, y)
plt.plot(x, 0 * x)
plt.show()  # 将绘制的函数图像窗口显示出来
