import pygame

# Size of window
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 500, 600
rectWidth, rectHeight = 100, 100

# Screen Color
screenColor = (190, 172, 158)
rectColor = (210, 195, 179)

pygame.init()

surface = pygame.display.set_mode(SCREEN_SIZE)

# Renderer called by game loop
def render_loop(gameBoard):

  surface.fill(screenColor)
  pygame.draw.rect(surface, (45,36,26), pygame.Rect(0, 100, 500, 500))
  for i in range(4):
    for j in range(4):
      rect = gameBoard[i][j]
      pygame.draw.rect(surface, rect.color, rect.rect)
      if rect.value is not 0:
        numLabel = pygame.font.Font("ClearSans-Bold.ttf",60-(7*len(str(rect.value))))
        surface.blit(
          numLabel.render(str(rect.value), 
          True, 
          (0,0,0)),
          (int(rect.rect.x + (rectWidth / 2) - (numLabel.size(str(rect.value))[0] / 2)),
          int(rect.rect.y + (rectHeight / 2)- (numLabel.size(str(rect.value))[1] / 2)))
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
