import pygame, sys
from viewClass import render_loop,slide
from modelClass import gameBoard
from controllerClass import controls, shouldRun
from modelClass import spawnRect, gameStart
from cRectangle import cRectangle

state = False
firstRun = True
test = { 
  0: [
    {'r':
    [cRectangle(0, 0, 100, 100, (240,228,217), 2), cRectangle(3, 0, 100, 100, (240,228,217), 2)]}
  ],
  1: [
    {'r':
    [cRectangle(0, 1, 100, 100, (240,228,217), 2), cRectangle(3, 1, 100, 100, (240,228,217), 2)]}
  ],
  2: [
    {'r':
    [cRectangle(0, 2, 100, 100, (240,228,217), 2), cRectangle(3, 2, 100, 100, (240,228,217), 2)]}
  ],
  3: [
    {'r':
    [cRectangle(0, 3, 100, 100, (240,228,217), 2), cRectangle(3, 3, 100, 100, (240,228,217), 2)]}
  ] 
}  
# Game Loop
while True:
  #initializing the board
  if firstRun:
    gameStart()
    firstRun = False
  

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
  #test
  slide(test)