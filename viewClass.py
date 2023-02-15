import pygame

# Size of window
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 500, 600

# Screen Color
screenColor = (190, 172, 158)
rectColor = (210, 195, 179)

pygame.init()

surface = pygame.display.set_mode(SCREEN_SIZE)

#creating a Title
def render_title():
  font = pygame.font.Font(None,100)
  title = font.render('2048',True,(0,0,0))
  surface.blit(title,(170,20))
