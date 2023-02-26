import pygame, sys
from viewClass import render_loop
from modelClass import gameBoard
from controllerClass import controls, shouldRun
from modelClass import spawnRect

state = False

# Game Loop
while True:

  for event in pygame.event.get():

    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

    if controls(event):
      if shouldRun(state):
        gameBoard = spawnRect(gameBoard)
        for x in range(4):
          for y in range(4):
            print(f'({x}, {y}): {gameBoard[x][y].value}')
      
  render_loop(gameBoard)