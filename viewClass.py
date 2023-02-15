import pygame

# Size of window
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 500, 600

# Screen Color
screenColor = (190, 172, 158)
rectColor = (210, 195, 179)

pygame.init()

surface = pygame.display.set_mode(SCREEN_SIZE)

# Renderer called by game loop
def render_loop(rect):
  surface.fill(screenColor)
  for i in range(4):
    for j in range(4):
      pygame.draw.rect(surface, rectColor, rect[i][j])
    
  render_title()
  pygame.display.update()

#creating a Title
def render_title():
  font = pygame.font.Font(None,100)
  title = font.render('2048',True,(0,0,0))
  surface.blit(title,(140,20))