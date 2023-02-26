import pygame
import time
# Size of window
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 500, 600

# Screen Color
screenColor = (190, 172, 158)
rectColor = (210, 195, 179)

pygame.init()

surface = pygame.display.set_mode(SCREEN_SIZE)

# Renderer called by game loop
def render_loop(gameBoard):
  numLabel = pygame.font.Font(None,100)

  surface.fill(screenColor)
  pygame.draw.rect(surface, (45,36,26), pygame.Rect(0, 100, 500, 500))
  for i in range(4):
    for j in range(4):
      rect = gameBoard[i][j]
      pygame.draw.rect(surface, rect.color, rect.rect)
      if rect.value is not 0:
        surface.blit(
          numLabel.render(str(rect.value), 
          True, 
          (0,0,0)), 
          (rect.rect.x+30, rect.rect.y+20)
          )
        
    
  render_title()
  pygame.display.update()

#creating a Title
def render_title():
  font = pygame.font.Font("ClearSans-Bold.ttf",80)
  title = font.render('2048',True,(0,0,0))

  surface.blit(title,(
    (SCREEN_WIDTH / 2) - (font.size('2048')[0] / 2),
    50 - (font.size('2048')[1] / 2)
    ))
  
rectPos = rectX, rectY = 100, 100
def slide(test):
  vel = 5
  for entry in list(test.keys()):
    dir = list(test[entry][0].keys())[0]
    numLabel = pygame.font.Font(None,100)
    xi, yi = test[entry][0][dir][0].rect.x, test[entry][0][dir][0].rect.y
    xf, yf = test[entry][0][dir][1].rect.x, test[entry][0][dir][1].rect.y
    while True:
      if xi != xf:
        if dir is 'r':
          xi += vel
        else:
          xi -= vel
      if yi != yf:
        if dir is 'd':
          yi += vel
        else:
          yi -= vel
      rect = pygame.Rect(xi, yi, 100, 100)
      pygame.draw.rect(surface, test[entry][0][dir][0].color, rect)
      surface.blit(
        numLabel.render(str(test[entry][0][dir][0].value), 
        True, 
        (0,0,0)), 
        (rect.x+30, rect.y+20)
        )
      pygame.display.update()
      if dir is 'r' or dir is 'l':
        if xi == xf:
          break
      if dir is 'u' or dir is 'd':
        if yi == yf:
          break
      
  


      



