#pylint: disable=no-member

import pygame

pygame.init()

bodyfont = pygame.font.Font('VT323-Regular.ttf', 30)

screen = pygame.display.set_mode((800,480))
screen_center = screen.get_rect().center



text_surface = bodyfont.render('Hello, World!', True, (255, 255, 255)) # White text
Base_DOD_Logo  = pygame.image.load('Assets\DOD_Logo.PNG').convert_alpha()
Large_DOD_Logo = pygame.transform.scale(Base_DOD_Logo, (240,240))
XLarge_DOD_Logo = pygame.transform.scale(Base_DOD_Logo, (480,480))

XLDOD_Rect = XLarge_DOD_Logo.get_rect()



running = True
while running: 



  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  #screen.blit(text_surface)

  #screen.blit(Base_DOD_Logo, (120,120))
  #screen.blit(Large_DOD_Logo, (120,120))
  screen.blit(XLarge_DOD_Logo, ((800-480)/2, 0))

  pygame.display.flip()

pygame.quit()










