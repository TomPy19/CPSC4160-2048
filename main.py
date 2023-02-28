import pygame, sys
from bin.viewClass import render_loop,hasWon
from bin.modelClass import gameBoard,score
from bin.controllerClass import controls,shouldRun,getDecision
from bin.modelClass import checkFull,checkWin,checkLose,handleKeypress,startGame
from importlib import reload
import bin.keepScore

state = False    # Boolean to check if space is being held
lost = False     # Boolean to check if game has ended in loss
won = False      # Boolean to check if game has ended in win
gameStart = True # Boolean to check if game should be restarted
highScore = bin.keepScore.highScore # Store high score from file

# Game Loop
while True:
  # Start game and initialize board
  if gameStart:
    startGame(gameBoard)
    gameStart = False

  # Update high score in real time
  if score['score'] > highScore:
    highScore = score['score']

  # Event checking loop
  for event in pygame.event.get():
    # If exit button is pressed, quit game
    if event.type == pygame.QUIT:
      bin.keepScore.saveScore(score) # Save high score
      pygame.quit()
      sys.exit()

    # Check condition of game state
    if checkWin(gameBoard):
      # Set won to True if 2048 is on the board
      won = True
      # Display winning message
      hasWon(True)
    if checkFull(gameBoard):
      # Check lose in all directions and store if game is not lost yet
      dirs = ['r','l','u','d']
      hasLost = True
      for i in dirs:
        if not checkLose(gameBoard, i):
          hasLost = False
      lost = hasLost
    if lost:
      # Display loss message
      hasWon(False)

    # Logic to restart game after a loss or win
    if lost or won:
      # Get keyboard input
      decision = getDecision()
      if decision:
        if decision == 'space': # Restart game on space press
          gameStart = True
          lost = False
          won = False
        if decision == 'esc': # Exit game on esc press
          pygame.quit()
          sys.exit()
        bin.keepScore.saveScore(score)
        reload(bin.keepScore) # Re-read high score file after saving
      
    
    # Obtain direction of button press
    dir = controls(event)

    # Only run if a keypress happens
    if dir != None:
      # Only run once even if a keypress is held down
      if shouldRun(state, dir):
        # Control all logic based off of direction
        moveList = handleKeypress(dir, gameBoard, score)
        
  # Only redner board if game has not ended in win or loss yet
  if not won and not lost:
    render_loop(gameBoard, score, highScore)
