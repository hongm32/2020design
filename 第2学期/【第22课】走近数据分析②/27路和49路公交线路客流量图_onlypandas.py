import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import rcParams


# 指定默认字体，负号显示问题
rcParams['font.sans-serif'] = ['SimHei']
rcParams['axes.unicode_minus'] = False

df = pd.read_excel("27路和49路公交线路客流量表.xlsx", header=1)
df.set_index("时间段", inplace=True)
df.plot.bar()

plt.show()  # 显示
