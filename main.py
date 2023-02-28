import pygame, sys
from viewClass import render_loop,hasWon
from modelClass import gameBoard
from controllerClass import controls, shouldRun
from modelClass import checkFull,checkWin,checkLose
import time
from modelClass import handleKeypress

state = False
lost = False
won = False
# Game Loop
while True:
  #test
  #slide(test)
  #time.sleep(3)
  if checkWin(gameBoard):
    won = True
    hasWon(True)
  if checkFull(gameBoard):
    dirs = ['r','l','u','d']
    lostDirs = []
    for i in dirs:
      if checkLose(gameBoard, i):
        lostDirs.append(True)
      else:
        lostDirs.append(False)
    if False not in lostDirs:
      lost = True
      # time.sleep(1)
  if lost:
    hasWon(False)
    # time.sleep(1)

  #initializing the board
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    
    dir = controls(event)

    if dir != None:
      if shouldRun(state, dir):
        moveList = handleKeypress(dir, gameBoard)
        
  if not won and not lost:
    render_loop(gameBoard)
