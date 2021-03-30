import pygame
import random


class Simley(pygame.sprite.Sprite):
    xvel = 1
    yvel = 1
    scale = 100
    def __init__(self, pos, xvel, yvel):
        pygame.sprite.Sprite.__init__(self)
        self.pos = pos
        self.image = pic
        self.scale = random.randrange(20, 100)
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


BLACK = (0, 0, 0)
pygame.init()
screen = pygame.display.set_mode([800, 600])
pygame.display.set_caption("消灭新冠病毒")
pic = pygame.image.load("xg.png")
bground = pygame.image.load("back.jpg")
colorkey = pic.get_at((0, 0))
pic.set_colorkey(colorkey)
keep_going = True
clock = pygame.time.Clock()
sprite_list = pygame.sprite.Group()
count = 0
mousedown = False
while keep_going:
    for event in pygame.event.get():  # 处理用户事件
        if event.type == pygame.QUIT:
            keep_going = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousedown = True
            pos = pygame.mouse.get_pos()
            clicked_smileys = []
            for s in sprite_list:
                if s.rect.collidepoint(pos):
                    clicked_smileys.append(s)
            for item in clicked_smileys:
                sprite_list.remove(item)
        if event.type == pygame.MOUSEBUTTONUP:
            mousedown = False
    screen.blit(bground, (0, 0))
    sprite_list.update()
    sprite_list.draw(screen)
    pygame.display.update()
    clock.tick(60)
    count += 1
    if count % 60 == 0:
        speedx = random.randint(-5, 5)
        speedy = random.randint(-5, 5)
        sposx = random.randint(0, 800)
        sposy = random.randint(0, 600)
        spos = (sposx, sposy)
        newSimply = Simley(spos, speedx, speedy)
        sprite_list.add(newSimply)

pygame.quit()
