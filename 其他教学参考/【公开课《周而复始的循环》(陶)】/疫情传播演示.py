import numpy as np
import matplotlib.pyplot as plt


class VirusSimulator(object):
    def __init__(self, radius=5, rate=0.5):
        self.width = 1000  # 地图宽度
        self.pop = 5000  # 总人口
        self.first_patients = 1  # 初始病人数量
        self.infection_radius = radius  # 感染半径
        self.infection_potential = rate  # 感染几率 10%
        self.locations = np.random.rand(self.pop, 2) * self.width  # 人群：横坐标、纵坐标
        self.status = np.array(["g"] * self.pop)  # 状态：（g-正常、r-感染）
        self.init_patients()  # 初始化感染群

    # 更新人群位置
    # 限制人群移动范围在 [0, self.width, 0, self.width]
    def move(self):
        self.locations += np.random.randn(self.pop, 2) * self.width
        # 所有超过边界的人，需要边界反弹
        # 左下角两条边
        n = self.locations[self.locations < 0].size
        self.locations[self.locations < 0] = np.random.rand(n) * self.width
        # 右上角两条边
        n = self.locations[self.locations > self.width].size
        self.locations[self.locations > self.width] = self.width - np.random.rand(n) * self.width

    # 初始化患病人群
    def init_patients(self):
        self.status[np.random.choice(self.pop, size=self.first_patients, replace=False)] = "r"

    # 统计感染人群
    @property
    def patients(self):
        return self.locations[self.status == "r"]

    # 统计感染人数
    @property
    def patients_num(self):
        return self.status[self.status == "r"].size

    # 传染函数
    def affect(self):
        for ip in self.patients:
            # 人与人的距离矩阵
            d = np.sqrt(np.sum(np.asarray(ip - self.locations)**2, axis=1))
            # 传染几率的矩阵
            p = np.random.rand(len(d))
            # 既小于传染距离又达到传染几率的人群
            self.status[(d < self.infection_radius) & (p < self.infection_potential)] = "r"

    # 统计人数
    def report_statistic(self, n):
        current_patient_num = self.patients_num
        print("第【{}】轮感染，总人数：{}，传染人数：{}".format(n, self.pop, current_patient_num))
        n += 1
        return current_patient_num, n

    # 显示函数
    def display(self):
        k, n = self.report_statistic(1)
        plt.ion()
        fig = plt.figure(figsize=(10, 5))

        ax1 = fig.add_subplot(1, 2, 1)
        ax2 = fig.add_subplot(1, 2, 2)

        x = np.array(n)
        y = np.array(k)

        while k < self.pop * 0.9:
            ax1.cla()
            # 画离散点
            ax1.scatter(self.locations[:, 0], self.locations[:, 1], c=self.status, s=1)
            # 限制图像范围
            ax1.axis([0, self.width, 0, self.width])
            self.move()
            self.affect()
            k, n = self.report_statistic(n)

            # 统计曲线
            ax2.cla()
            x = np.append(x, n)
            y = np.append(y, k)
            ax2.plot(x, y, 'o-', color='r', label="Round:{}  Infected:{}".format(n - 1, k))
            ax2.axis([0, 100, 0, self.pop])
            plt.legend(loc='best')

            plt.pause(0.1)

        plt.ioff()
        plt.show()


if __name__ == "__main__":
    vs = VirusSimulator(radius=5, rate=0.5)  # radius:感染半径 rate：感染比例
    vs.display()
