import pygame, sys
from viewClass import render_loop
from modelClass import gameBoard
from controllerClass import new_rect
from modelClass import spawnRect

# Game Loop
while True:

  for event in pygame.event.get():

    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

    if(new_rect()):
      gameBoard = spawnRect(gameBoard)
      print(new_rect)
      
  render_loop(gameBoard)