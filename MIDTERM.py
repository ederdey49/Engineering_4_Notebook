import pygame
import random

pygame.init()


screen = pygame.display.set_mode([1000,1000])

running = True


pygame.display.set_caption('hello world')
screen.fill([65, 105, 225])

pygame.display.flip()

for i in range(0, 4096):
        pygame.draw.rect(screen, [int(random.random()*255), int(random.random()*255),int(random.random()*255) ], (int(random.random()*1000), int(random.random()*1000), 10, 10))
        pygame.display.flip()

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
pygame.quit()
