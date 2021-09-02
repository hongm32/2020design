import numpy as np  # 加载numpy模块并取一个简洁的别名为np
import matplotlib.pyplot as plt


x = np.arange(0, 2 * np.pi, 0.01)   # x在0到2π之间，每隔0.01取一个点
y = np.sin(x)       # 通过解析式计算列表x对应的列表y的值
plt.plot(x, y)      # 绘制折线图
plt.show()          # 显示图表
