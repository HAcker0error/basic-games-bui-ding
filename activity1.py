import pygame
pygame.init()
screen = pygame.display.set_mode((400 , 600))

done = True

while not done :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

    pygame.draw.rect(screen (0 , 200 , 200) , pygame.rect(20 , 20 , 40 , 40))

    pygame.display.filp()