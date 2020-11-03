import pygame
from pygame.sprite import Sprite
from pygame.sprite import Group


class Settings:
    def __init__(self):
        """ 屏幕设置 """
        self.screen_width = 700
        self.screen_height = 400
        self.bg_color = (0, 160, 131)
        ''' 方块的设置 '''
        self.firstwidth = 200  # 第一方块的宽度
        self.item_height = 10  # 方块的高度
        self.item_middle = 15  # 方块之间的宽度间隔

        '''选中条块'''
        self.currentItem = None
        self.currentItemTower = None

        self.level = 3  # 游戏级别

        self.newGame = True  # 是否是新游戏
        self.gameStar = False  # 游戏是否开始
        self.star = 0  # 游戏步骤
        self.times = 30  # 闯关成功延时，单位0.1秒


class Button:
    def __init__(self, screen, msg):
        """ 按钮定义 """
        self.screen = screen

        self.width, self.height = (200, 50)
        self.button_color = (255, 0, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 24)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = screen.get_rect().center

        self.prep_msg(msg)

    def prep_msg(self, msg):
        """将msg渲染为图像，并使其在按钮上居中"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # 绘制一个用颜色填充的按钮，再绘制文本
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


class Scoreboard():
    """显示得分信息"""

    def __init__(self, pysettings, screen):
        """初始化显示得分属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.pysettings = pysettings

        # 显示得分信息时使用的字休设置
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()

    def prep_score(self):
        if str(self.pysettings.star)[0] == "&":
            score_str = "Success! Step:{} Level{}".format(str(self.pysettings.star)[1:], self.pysettings.level)
        else:
            score_str = "Step:{} Level{}".format(self.pysettings.star, self.pysettings.level)
        # score_str = "{},{}".format(self.pysettings.star, self.pysettings.level)
        self.score_image = self.font.render(score_str, True, self.text_color, self.pysettings.bg_color)

        # 将得分放在右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """在屏幕上显示得分"""
        self.screen.blit(self.score_image, self.score_rect)


class Tower(Sprite):
    def __init__(self, screen, pysettings, x, y):
        super(Tower, self).__init__()
        self.image = pygame.image.load("tower.gif")
        self.rect = self.image.get_rect()

        self.screen = screen
        self.rect.x = x
        self.rect.y = y + self.rect.height
        self.settings = pysettings
        # 当前的方块
        self.items = []

    def draw_tower(self):
        """ 绘制塔"""
        self.screen.blit(self.image, self.rect)

    def addItem(self, item):
        """ 添加方块"""
        self.items.append(item)

    def remove(self, item):
        """ 去掉当前的方块"""
        self.items.remove(item)

    def getLastItem(self):
        """获取最上面一个条块"""
        if len(self.items) == 0:
            return None
        return self.items[-1]

    def getNextItemPosition(self, item):
        """ 获取条块位置"""
        posx = self.rect.x + (self.rect.width - item.width) / 2
        posy = self.getNextItemPositionY()
        width = item.width
        height = item.height
        return posx, posy, width, height

    def getNextItemPositionY(self):
        """ 获取下一方块的Y"""
        return self.rect.height - (self.settings.item_height + 3) * len(self.items) + 165

    def getCurrentY(self, item):
        if item.getChoose():
            return self.rect.height - (self.settings.item_height + 3) * (len(self.items) - 1) + 165


class Item(Sprite):
    def __init__(self, screen, pysettings, tower, width):
        super(Item, self).__init__()
        self.__isChoose = False  # 条块当前是否选中
        self.screen = screen
        self.width = width
        self.height = pysettings.item_height
        self.color = (255, 0, 255)
        self.rect = pygame.Rect(tower.getNextItemPosition(self))
        tower.addItem(self)

    def draw_item(self):
        """ 画方块"""
        self.screen.fill(self.color, self.rect)

    def getChoose(self):
        """ 获取条块是否选中"""
        return self.__isChoose

    def setChoose(self, isChoose):
        """ 设置条块是否选中"""
        self.__isChoose = isChoose


def update_screen(screen, pySettings, towers, items, play_button, scoreBoard):
    """ 屏幕更新"""
    screen.fill(pySettings.bg_color)
    if pySettings.gameStar == False:
        play_button.draw_button()
    else:
        ''' 绘制tower'''
        for tower in towers:
            tower.draw_tower()

        for item in items:
            item.draw_item()
        scoreBoard.show_score()

    # 让最近绘制的屏幕可见
    pygame.display.flip()
    success(towers, pySettings)


def check_event(screen, pysettings, towers, play_button):
    """ 响应按键和鼠标事件 """
    # 如果不添加这个get,则界面会卡死
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            import sys
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if pysettings.gameStar:
                chekc_mouseDown(screen, pysettings, towers, mouse_x, mouse_y)
            else:
                check_playbutton(play_button, pysettings, mouse_x, mouse_y)


def chekc_mouseDown(screen, pysettings, towers, mouse_x, mouse_y):
    """ 检查鼠标按下事件"""
    for tower in towers:
        if tower.rect.collidepoint(mouse_x, mouse_y):
            # 当前操作的是同一个塔
            if pysettings.currentItemTower == tower:
                item = tower.getLastItem()
                if item is None:
                    break
                if item.getChoose():  # 当前是选中方块，则还原
                    item.rect.y = tower.getCurrentY(item)
                    item.setChoose(False)
                    pysettings.currentItem = None
                else:
                    item.rect.y = tower.rect.y
                    item.setChoose(True)
                    pysettings.currentItemTower = tower
                    pysettings.currentItem = item
            else:  # 不是同一个塔
                currentItem = tower.getLastItem()
                if pysettings.currentItem is None:
                    if currentItem is None:
                        break
                    else:
                        currentItem.rect.y = tower.rect.y
                        currentItem.setChoose(True)
                        pysettings.currentItemTower = tower
                        pysettings.currentItem = currentItem
                else:
                    # 获取当前塔下的方块
                    item = pysettings.currentItemTower.getLastItem()
                    if currentItem is None or currentItem.rect.width > item.rect.width:
                        item.rect = pygame.Rect(tower.getNextItemPosition(item))
                        item.setChoose(False)
                        tower.addItem(item)
                        pysettings.currentItemTower.remove(item)
                        pysettings.currentItemTower = tower
                        pysettings.currentItem = None
                        record(pysettings)


def check_playbutton(play_button, pysettings, mouse_x, mouse_y):
    """检查按钮是否被按下"""
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        pysettings.gameStar = True


def createTower(screen, pysettings):
    """ 添加3个塔 """
    towers = Group()
    towerA = Tower(screen, pysettings, 40, 00)
    towers.add(towerA)
    towerB = Tower(screen, pysettings, 250, 00)
    towers.add(towerB)
    towerC = Tower(screen, pysettings, 460, 00)
    towers.add(towerC)
    return towers


def createItem(screen, pysettings, tower, number):
    """ 创建方块 """
    items = Group()
    star = 0
    while star < number:
        item = Item(screen, pysettings, tower, pysettings.firstwidth - star * 20)
        items.add(item)
        star += 1
    return items


def success(towers, pysettings):
    """ 判断是否成功 第一 二个塔的方块数为0 """
    towerCopy = towers.sprites()
    if len(towerCopy[0].items) == 0 and len(towerCopy[1].items) == 0:
        if pysettings.times == 0:
            pysettings.times = pysettings.Times
            towerCopy[0].items.clear()
            towerCopy[1].items.clear()
            towerCopy[2].items.clear()
            pysettings.level += 1
            pysettings.newGame = True  # 闯关成功是否继续
            pysettings.star = 0  # 重置记数器
        else:
            pysettings.times -= 1
            if str(pysettings.star)[0] != "&":
                pysettings.star = "&{}".format(pysettings.star)
            pygame.time.delay(100)


def record(pysettings):
    pysettings.star += 1  # 游戏步骤加1


def run_game():
    pygame.init()
    pysetting = Settings()
    pysetting.Times = pysetting.times
    pygame.display.set_caption("汉诺塔游戏--by 学虹")
    screen = pygame.display.set_mode((pysetting.screen_width, pysetting.screen_height))
    towers = createTower(screen, pysetting)
    items = None
    play_button = Button(screen, "Start")
    # 开始游戏
    while True:
        if pysetting.newGame:
            items = createItem(screen, pysetting, towers.sprites()[0], pysetting.level)
            pysetting.currentItemTower = towers.sprites()[0]
            pysetting.newGame = False
        scoreBoard = Scoreboard(pysetting, screen)
        check_event(screen, pysetting, towers, play_button)
        update_screen(screen, pysetting, towers, items, play_button, scoreBoard)


run_game()
