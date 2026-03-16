#pylint: disable=no-member

import pygame

pygame.init()

bodyfont = pygame.font.Font('VT323-Regular.ttf', 30)

screen = pygame.display.set_mode((800,480))

running = True
while running: 

  text_surface = bodyfont.render('Hello, World!', True, (255, 255, 255)) # White text

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen.blit(text_surface)

  pygame.display.flip()

pygame.quit()










