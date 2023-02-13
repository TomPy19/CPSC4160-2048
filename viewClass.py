import pygame, sys

# Size of window
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 500, 600

# Screen Color
screenColor = (190, 172, 158)
rectColor = (210, 195, 179)
rectSize = rectWidth, rectHeight = 100, 100
rectPos = rectX, rectY = 100, 100

pygame.init()
# pygame.display.init()
gameBoard = {}

for x in range(4):
  gameBoard[x] = {}
  for y in range(4):
    gameBoard[x][y] = (pygame.Rect(20+(x*120), 120+(y*120), 100, 100))



surface = pygame.display.set_mode(SCREEN_SIZE)

gameRect = pygame.Rect(rectX, rectY, rectWidth, rectHeight)

rectSpeed = 50

def move_rect(Rect):
  keys = pygame.key.get_pressed()
  if keys[pygame.K_LEFT] and Rect.left > 0:
    gameRect.move_ip(-rectSpeed,0)
  if keys[pygame.K_RIGHT] and Rect.right < SCREEN_WIDTH:
    gameRect.move_ip(rectSpeed,0)
  if keys[pygame.K_UP] and Rect.top > 0:
    gameRect.move_ip(0,-rectSpeed)
  if keys[pygame.K_DOWN] and Rect.bottom < SCREEN_HEIGHT:
    gameRect.move_ip(0,rectSpeed)

# Game loop
while True:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    move_rect(gameRect)
  
  surface.fill(screenColor)
  for i in range(4):
    for j in range(4):
      pygame.draw.rect(surface, rectColor, gameBoard[i][j])
  
  pygame.display.update()