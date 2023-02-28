import pygame, sys
from viewClass import render_loop,slide,hasWon
from modelClass import gameBoard
from controllerClass import controls, shouldRun
from modelClass import spawnRect, gameStart,checkFull,checkWin
from cRectangle import cRectangle
import time
from modelClass import handleKeypress

state = False
firstRun = True
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
      
    #test
    #slide(test)
    #time.sleep(3)
    if checkFull(gameBoard):
      hasWon(False)
      time.sleep(1)
    if checkWin(gameBoard):
      hasWon(True)
      time.sleep(1)
      
    dir = controls(event)

    if dir != None:
      if shouldRun(state, dir):
        moveList = handleKeypress(dir, gameBoard)

 render_loop(gameBoard)
