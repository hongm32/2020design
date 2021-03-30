import pygame  # 导入模块
import sys
import random


def showfu(x0, y0):
    # 定义函数，在(x,y)位置显示福字
    gift = pygame.image.load('fu.png')  # 加载福字图像
    screen.blit(gift, [x0, y0])  # 将福字显示在(x,y)位置上


def showscore(score0):
    # 定义函数,显示分数
    textfont = pygame.font.SysFont('Arial', 30)  # 创建文本对象，Arial，大小30
    t = textfont.render('score:' + str(score0), True, (255, 0, 0))  # 生成平滑的红色字符串
    screen.blit(t, [50, 50])  # 在窗口显示


# 主程序开始
pygame.init()  # 初始化
score = 0  # 变量初始化
mousex = 0
mousey = 0

screen = pygame.display.set_mode([800, 600])  # 创建一个窗口
pygame.display.set_caption('接福')  # 设置窗口标题
back = pygame.image.load('bj.jpg')  # 加载背景图像
screen.blit(back, [0, 0])  # 将背景图显示在窗口
showscore(score)  # 显示分数

x = random.randint(50, 700)  # 随机生成福字水平方向坐标
y = random.randint(50, 500)  # 随机生成福字垂直方向坐标
showfu(x, y)  # 在(x,y)位置显示福字
pygame.display.update()  # 刷新窗口

while True:
    for event in pygame.event.get():  # 侦听并获取事件列表
        if event.type == pygame.QUIT:  # 接收到退出事件后退出程序
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:  # 侦听到鼠标点击事件
            mousex, mousey = pygame.mouse.get_pos()  # 获取鼠标按下的坐标
            # 判断鼠标是否击中福字，本例福字宽为60，高为70
            if mousex in range(x, x + 60) and mousey in range(y, y + 70):
                score = score + 5  # 加分

    screen.blit(back, [0, 0])  # 将背景图显示在窗口
    showscore(score)  # 显示分数
    x = random.randint(50, 700)  # 随机生成福字水平方向坐标
    y = random.randint(50, 500)  # 随机生成福字垂直方向坐标
    showfu(x, y)  # 在(x,y)位置显示福字
    pygame.display.update()  # 刷新窗口
    pygame.time.delay(800)  # 延时
