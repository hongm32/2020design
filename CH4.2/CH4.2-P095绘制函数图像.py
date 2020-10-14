# 4.2.1：P095-绘制函数图像
import numpy as np  # 加载numpy模块并取名为np
# 下面的魔法命令表示集成绘画工具matplotlib内嵌到Jupyter notebook中
# %matplotlib inline
import matplotlib.pyplot as plt  # 加载matplotlib.pyplot并取名为plt
from matplotlib.font_manager import FontProperties
font = FontProperties(fname='C:/Windows/Fonts/simhei.ttf', size=16)  # 用于解决中文字体问题

x = np.arange(0, 2*np.pi, 0.01)  # x在0到2π之间，每隔0.01取一个点
y1 = np.sin(x)  # 求sin(x)对应的y1值
y2 = np.sin(-x)  # 求sin(-x)对应的y2值
y3 = np.sin(2 * x) / 2  # 求sin(2x)/2对应的y3值
plt.plot(x, y1)  # 绘制sin(x)图像
plt.plot(x, y2)  # 绘制sin(-x)图像
plt.plot(x, y3)  # 绘制sin(2*x)/2图像
plt.title('正弦函数sin(x)', fontproperties=font)  # 设置图像标题
plt.xlabel('X')  # 设置X轴标题
plt.ylabel('Y')  # 设置Y轴标题
plt.show()  # 将绘制的函数图像窗口显示出来
input("运行完毕，请按回车键退出...")
