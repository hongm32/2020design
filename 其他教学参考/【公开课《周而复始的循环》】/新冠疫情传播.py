# 假如A被感染，前3天为潜伏期，不发作也不会传染人，
# 第4天开始发作，从发作到治愈需要7天时间，期间每天传染3个人
# 探究一下传播曲线

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


def covid(n):
    days = incubation + cure_period
    # 列表：潜伏期, 发病期, 发病, 治愈, 现存， 累计
    temp = [0 for _ in range(days + 4)]
    covid_count = [temp]
    for i in range(incubation):
        tmp = temp[:]
        tmp[i] = 1
        tmp[-2] = 1
        tmp[-1] = 1
        covid_count.append(tmp)
    for i in range(incubation + 1, n + 1):
        tmp = temp[:]
        for j in range(1, days):
            tmp[j] = covid_count[-1][j - 1]
        tmp[-4] = covid_count[-1][-4] + covid_count[-1][incubation - 1] - covid_count[-1][days - 1]
        # tmp[0] = tmp[-4] * rate
        tmp[0] = sum(tmp[incubation:(incubation + propagate)]) * rate
        tmp[-3] = covid_count[-1][-3] + covid_count[-1][days - 1]
        tmp[-2] = sum(tmp[:days])
        tmp[-1] = tmp[-2] + tmp[-3]
        covid_count.append(tmp)
    return covid_count


def save_csv():
    title_list = "周期,"
    for i in range(incubation):
        title_list += "潜伏_{},".format(i + 1)
    for i in range(cure_period):
        title_list += "发病_{},".format(i + 1)
    title_list += "发病,治愈,现存确诊,累计确诊"
    with open("新冠疫情传播.csv", "w") as f:
        f.write(title_list + "\n")
        for idx, val in enumerate(covid_list):
            tmp = str(idx)
            for i, value in enumerate(val):
                tmp += ",{}".format(value)
            f.write(tmp + "\n")


def report():
    x = []
    data_total = []
    data_count = []
    for idx, val in enumerate(covid_list):
        x.append(idx)
        data_total.append(val[-1] + val[-2])
        data_count.append(val[-1])
    font = FontProperties(fname='C:/Windows/Fonts/simhei.ttf', size=16)
    plt.xlim(-1, 24)
    plt.plot(x[:23], data_count[:23], "o-")
    plt.title('疫情发展预测', fontproperties=font)  # 设置图像标题
    plt.xlabel('周期(天)', fontproperties=font)  # 设置X轴标题
    plt.ylabel('现存确诊人数', fontproperties=font)  # 设置Y轴标题
    plt.savefig("新冠疫情传播.png")
    plt.show()


if __name__ == '__main__':
    rate = 3  # 传染率，即每天传染3人
    incubation = 3  # 潜伏期
    cure_period = 7  # 发病期
    propagate = 7  # 传染期
    covid_list = covid(60)
    save_csv()
    report()
