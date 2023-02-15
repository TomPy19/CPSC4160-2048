import pygame, sys
from viewClass import render_loop
from modelClass import gameBoard
import viewClass, controllerClass

# Game Loop
while True:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

  render_loop(gameBoard)