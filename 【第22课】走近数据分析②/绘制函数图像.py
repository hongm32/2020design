import numpy as np  # 加载numpy模块并取名为np
import matplotlib
import matplotlib.pyplot as plt  # 加载matplotlib.pyplot并取名为plt


# 指定默认字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

x = np.arange(-10, 12, 0.1)  # x在-10到12之间，每隔0.1取一个点
y = x ** 2 - 2 * x + 1
plt.plot(x, y)
plt.title('二次函数图像', size=18)  # 设置图像标题
plt.xlabel('X')  # 设置X轴标题
plt.ylabel('Y')  # 设置Y轴标题
plt.show()  # 将绘制的函数图像窗口显示出来

input("运行完毕，请按回车键退出...")
