import pygame
import random


def showtext(showtext, textpos, color):
    text_str = showtext
    text = font.render(text_str, True, color)
    text_rect = text.get_rect()
    text_rect.x = textpos[0]
    text_rect.y = textpos[1]
    screen.blit(text, text_rect)


def Pause():
    is_pause = True
    while is_pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit();
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    is_pause = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        font = pygame.font.SysFont("simsunnsimsun", 20)
        BLACK = (150, 25, 200)
        text_str = "按键P重新开始，按键Q退出游戏"
        text = font.render(text_str, True, BLACK)
        text_rect = text.get_rect()
        text_rect.centerx = screen.get_rect().centerx
        text_rect.y = 300
        screen.blit(text, text_rect)
        pygame.display.update()
        clock.tick(60)


class Simley(pygame.sprite.Sprite):
    xvel = 1
    yvel = 1
    scale = 100

    def __init__(self, pos, xvel, yvel):
        pygame.sprite.Sprite.__init__(self)
        self.pos = pos
        self.image = pic
        self.scale = random.randrange(20, 150)
        self.xvel = xvel
        self.yvel = yvel
        self.image = pygame.transform.scale(self.image, (self.scale, self.scale))
        self.rect = self.image.get_rect()
        self.rect.x = pos[0] - self.scale / 2
        self.rect.y = pos[1] - self.scale / 2

    def update(self):
        self.rect.x += self.xvel
        self.rect.y += self.yvel
        if self.rect.x <= 0 or self.rect.x + self.scale > screen.get_width():
            self.xvel = -self.xvel
        if self.rect.y <= 0 or self.rect.y + self.scale > screen.get_height():
            self.yvel = -self.yvel


pygame.init()
screen = pygame.display.set_mode([800, 600])
pygame.display.set_caption("消灭新冠病毒")
pic = pygame.image.load("xg.png")
bground = pygame.image.load("back.jpg")
font = pygame.font.SysFont("simsunnsimsun", 26)
BLACK = (0, 0, 0)
colorkey = pic.get_at((0, 0))
pic.set_colorkey(colorkey)
keep_going = True
clock = pygame.time.Clock()
sprite_list = pygame.sprite.Group()

count = 0
cov_count = 0
clicked_smileys_count = 0
score = 0
time_count = 60
mousedown = False
while keep_going:
    for event in pygame.event.get():  # 处理用户事件
        if event.type == pygame.QUIT:
            keep_going = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                Pause()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mousedown = True
            pos = pygame.mouse.get_pos()
            clicked_smileys = []
            for s in sprite_list:
                if s.rect.collidepoint(pos) == True:
                    clicked_smileys.append(s)
                    score += 5
            for item in clicked_smileys:
                sprite_list.remove(item)
            clicked_smileys_count += len(clicked_smileys)
        if event.type == pygame.MOUSEBUTTONUP:
            mousedown = False
    # screen.fill(BLACK)
    screen.blit(bground, (0, 0))

    if time_count == 0:
        text_str = "游戏结束，你的得分为：" + str(score)
        showtext(text_str, [200, 10], BLACK)
        Pause()
    else:
        text_str = "病毒总数：" + str(cov_count) + "  剩余病毒：" + str(cov_count - clicked_smileys_count) + "  当前得分" + str(
            score) + " 剩余时间" + str(time_count)
        showtext(text_str, [50, 10], BLACK)

    sprite_list.update()
    sprite_list.draw(screen)
    pygame.display.update()
    clock.tick(60)
    count += 1
    if count % 30 == 0 and (cov_count - clicked_smileys_count) < 50:
        if count % 60 == 0:
            time_count -= 1

        speedx = random.randint(-5, 5)
        speedy = random.randint(-5, 5)
        # spos = pygame.mouse.get_pos()
        sposx = random.randint(0, 800)
        sposy = random.randint(0, 600)
        spos = (sposx, sposy)
        newSimply = Simley(spos, speedx, speedy)
        cov_count += 1
        sprite_list.add(newSimply)

Pause()
