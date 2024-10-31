import pygame, sys, time

pygame.init()
WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("christmas card animation")
screen.fill("white")

snowman = pygame.image.load("snowman.png")
snowman_resized = pygame.transform.scale(snowman, (WIDTH, HEIGHT))

xmas_tree = pygame.image.load("xmas_tree.png")
xmas_tree_resized = pygame.transform.scale(xmas_tree, (WIDTH, HEIGHT))

merry_xmas = pygame.image.load("merry_xmas.png")
merry_xmas_resized = pygame.transform.scale(merry_xmas, (WIDTH, HEIGHT))


pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    screen.blit(snowman_resized, (0,0))
    font = pygame.font.SysFont("Times New Roman", 70)
    text = font.render("Merry Christmas!", True, (2, 153, 17))
    screen.blit(text, (75,200))
    pygame.display.update()
    time.sleep(3)

    screen.blit(xmas_tree_resized, (0,0))
    font1 = pygame.font.SysFont("Times New Roman", 22)
    text1 = font1.render("Wishing you a very Merry Christmas and a happy new year!", True, (250, 19, 2))
    screen.blit(text1, (50,50))
    pygame.display.update()
    time.sleep(3)

    screen.blit(merry_xmas_resized, (0,0))
    pygame.display.update()
    time.sleep(3)