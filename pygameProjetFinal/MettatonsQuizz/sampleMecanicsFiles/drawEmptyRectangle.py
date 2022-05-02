import pygame

pygame.init()
  
surface = pygame.display.set_mode((400,300))
  
color = (252,104,4)


pygame.draw.rect(surface, color, pygame.Rect(30, 30, 240, 100),  5)
while True:
    pygame.display.flip()