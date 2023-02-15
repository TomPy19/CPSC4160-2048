import pygame, sys
import modelClass, viewClass, controllerClass

# Game Loop
while True:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
  
  viewClass.surface.fill(viewClass.screenColor)
  for i in range(4):
    for j in range(4):
      pygame.draw.rect(viewClass.surface, viewClass.rectColor, modelClass.gameBoard[i][j])
  
  pygame.display.update()