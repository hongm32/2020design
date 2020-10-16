import pygame


pygame.init()
screen = pygame.display.set_mode([600, 400])
screen.fill((144, 238, 144))
img = pygame.image.load('ball.png')
screen.blit(img, [200, 200])
pygame.display.update()
input("运行完毕，请按回车键退出...")
