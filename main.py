import pygame, sys
from viewClass import render_loop
from modelClass import gameBoard
from controllerClass import controls, shouldRun
from modelClass import handleKeypress

state = False

# Game Loop
while True:

  for event in pygame.event.get():

    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

    dir = controls(event)

    if dir != None:
      if shouldRun(state, dir):
        moveList = handleKeypress(dir, gameBoard)
        print (moveList)
      
  render_loop(gameBoard)