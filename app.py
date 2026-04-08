#pylint: disable=no-member

import pygame





pygame.init()

bodyfont = pygame.font.Font('VT323-Regular.ttf', 30)

screen = pygame.display.set_mode((800,480), pygame.FULLSCREEN) 
screen_center = screen.get_rect().center




# asset testing
text_surface = bodyfont.render('Hello, World!', True, (255, 255, 255)) # White text
Base_DOD_Logo  = pygame.image.load('Assets/DOD_Logo.PNG').convert_alpha()
Large_DOD_Logo = pygame.transform.scale(Base_DOD_Logo, (240,240))
XLarge_DOD_Logo = pygame.transform.scale(Base_DOD_Logo, (480,480))

XLDOD_Rect = XLarge_DOD_Logo.get_rect()

#loading bar spritesheet
#LoadingBar_Sheet = pygame.image.load('Assets/Loading.PNG').convert_alpha()
#LoadingBarFrame = LoadingBar_Sheet.images_at((0,0,200,50), (201,0,200,50),(401,0,200,50), (601,0,200,50),
#                                            (801,0,200,50), (1001,0,200,50),(1201,0,200,50),
#                                            (1401,0,200,50),(0,51,200,50), (201,51,200,50),(401,51,200,50))





running = True
while running: 



  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  #screen.blit(text_surface)

  #screen.blit(Base_DOD_Logo, (120,120))
  #screen.blit(Large_DOD_Logo, (120,120))
  screen.blit(XLarge_DOD_Logo, ((800-480)/2, 0))

  #screen.blit(LoadingBarFrame[2])


  pygame.display.flip()

pygame.quit()


