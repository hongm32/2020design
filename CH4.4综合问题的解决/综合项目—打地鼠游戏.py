import pygame  # 导入模块
import sys
import random


class Mice:
    # 地鼠类
    def __init__(self):
        self.image = pygame.image.load('dishu.png')  # 加载地鼠图像
        self.x = random.randint(50, 700)  # 产生水平方向随机坐标
        self.y = random.randint(50, 400)  # 产生垂直方向随机坐标


def showscore(fenshu):
    # 定义函数,显示分数
    textfont = pygame.font.SysFont('Arial', 30)  # 创建文本对象，Arial，大小30
    t = textfont.render('score:' + str(fenshu), True, (255, 0, 0))  # 生成平滑的红色字符串
    screen.blit(t, (20, 20))  # 在窗口显示


# 主程序开始
pygame.init()  # 初始化
screen = pygame.display.set_mode([800, 500])  # 创建一个窗口
pygame.display.set_caption('打地鼠')  # 设置窗口标题
back = pygame.image.load('tudi.jpg')  # 加载背景图像

score = 0  # 变量初始化
mousex = 0
mousey = 0

screen.blit(back, [0, 0])  # 将背景图显示在窗口
showscore(score)  # 显示分数
mice = Mice()  # 生成一个地鼠实例
screen.blit(mice.image, [mice.x, mice.y])  # 显示地鼠
pygame.display.update()  # 刷新窗口

while True:
    for event in pygame.event.get():  # 侦听并获取事件列表
        if event.type == pygame.QUIT:  # 接收到退出事件后退出程序
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:  # 侦听到鼠标点击事件
            mousex, mousey = pygame.mouse.get_pos()  # 获取鼠标按下的坐标
            # 判断鼠标是否击中地鼠，本例地鼠宽为200，高为200
            if mousex in range(mice.x, mice.x + 150) and mousey in range(mice.y, mice.y + 150):
                score = score + 5  # 加分

    screen.blit(back, [0, 0])  # 将背景图显示在窗口
    showscore(score)  # 显示分数
    mice = Mice()  # 生成一个地鼠实例
    screen.blit(mice.image, [mice.x, mice.y])  # 显示地鼠
    pygame.display.update()  # 刷新窗口
    pygame.time.delay(800)  # 延时
