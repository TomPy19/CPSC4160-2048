import pygame

# Size of window
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 500, 600
rectWidth, rectHeight = 100, 100

# Screen Color
screenColor = (190, 172, 158)
rectColor = (210, 195, 179)

# Board Specs
screenWidth = 0
borderRadius = 20
rectBorder = 10

# Initialize pygame
pygame.init()

# Set display surface
surface = pygame.display.set_mode(SCREEN_SIZE)

# Renderer called by game loop
def render_loop(gameBoard,score,highScore):

  # Fill background color
  surface.fill(screenColor)
  pygame.draw.rect(surface, (45,36,26), pygame.Rect(0, 100, 500, 500),screenWidth, borderRadius)
  # Display each gameboard cell
  for i in range(4):
    for j in range(4):
      rect = gameBoard[i][j]
      pygame.draw.rect(surface, rect.color, rect.rect,0,rectBorder)
      if rect.value is not 0:
        numLabel = pygame.font.Font("bin/fonts/ClearSans-Bold.ttf",60-(7*len(str(rect.value))))
        surface.blit(
          numLabel.render(str(rect.value), 
          True, 
          (0,0,0)),
          (int(rect.rect.x + (rectWidth / 2) - (numLabel.size(str(rect.value))[0] / 2)),
          int(rect.rect.y + (rectHeight / 2)- (numLabel.size(str(rect.value))[1] / 2)))
        )
        
  render_title() # Render '2048' Title
  render_scores(score['score'], highScore) # Render current score and high score
  pygame.display.update() # Update Display

#creating a Title
def render_title():
  font = pygame.font.Font("bin/fonts/ClearSans-Bold.ttf",70)
  title = font.render('2048',True,(0,0,0))

  surface.blit(title,(
    (SCREEN_WIDTH / 2) - (font.size('2048')[0] / 2),
    50 - (font.size('2048')[1] / 2)
    ))
  
# Display current score and high score
def render_scores(score,highScore):
  titleFont = pygame.font.Font("bin/fonts/ClearSans-Bold.ttf",20)
  scoreFont = pygame.font.Font("bin/fonts/ClearSans-Regular.ttf",20)

  scoreLabel = titleFont.render('Score:',True,(0,0,0))
  highScoreLabel = titleFont.render('High Score:',True,(0,0,0))

  scoreText = scoreFont.render(str(score),True,(0,0,0))
  highScoreText = scoreFont.render(str(highScore),True,(0,0,0))

  surface.blit(scoreLabel,(
    20,
    95 - (titleFont.size('Score')[1]+scoreFont.size(str(score))[1])+5
    ))
  surface.blit(highScoreLabel,(
    500 - (20+titleFont.size('High Score')[0]),
    95 - (titleFont.size('High Score')[1]+scoreFont.size(str(highScore))[1])+5
    ))
  surface.blit(scoreText,(
    20,
    95 - (scoreFont.size(str(score))[1])
    ))
  surface.blit(highScoreText,(
    500 - (20+scoreFont.size(str(highScore))[0]),
    95 - (scoreFont.size(str(highScore))[1])
    ))


#Movement animation (Unused)
def slide(test):
  vel = 20
  for entry in list(test.keys()):
    # print (list(test[str(entry)].keys())[0])
    dir = list(test[str(entry)].keys())[0]
    xi, yi = test[str(entry)][dir][0].rect.x, test[str(entry)][dir][0].rect.y
    xf, yf = test[str(entry)][dir][1].rect.x, test[str(entry)][dir][1].rect.y
    while True:
      if xi != xf:
        if dir is 'r':
          xi += vel
        else:
          xi -= vel
      if yi != yf:
        if dir is 'd':
          yi += vel
        else:
          yi -= vel
      rect = pygame.Rect(xi, yi, 100, 100)
      pygame.draw.rect(surface, test[str(entry)][dir][0].color, rect, 0, rectBorder)
      if test[str(entry)][dir][0].value != 0:
        numLabel = pygame.font.Font("bin/fonts/ClearSans-Bold.ttf",60-(7*len(str(test[str(entry)][dir][0].value))))
        surface.blit(
          numLabel.render(str(test[str(entry)][dir][0].value), 
          True, 
          (0,0,0)),
          (int(test[str(entry)][dir][0].rect.x + (rectWidth / 2) - (numLabel.size(str(test[str(entry)][dir][0].value))[0] / 2)),
          int(test[str(entry)][dir][0].rect.y + (rectHeight / 2)- (numLabel.size(str(test[str(entry)][dir][0].value))[1] / 2)))
        )
      pygame.display.update()
      if dir is 'r' or dir is 'l':
        if xi == xf:
          break
      if dir is 'u' or dir is 'd':
        if yi == yf:
          break

# Displaying win/lose message
def hasWon(win):
  rect = pygame.Rect(SCREEN_WIDTH/4, SCREEN_HEIGHT/2 - 50, 250, 100)
  pygame.draw.rect(surface, (210, 195, 179), rect, 0, rectBorder)
  font = pygame.font.Font("bin/fonts/ClearSans-Bold.ttf",45)
  font2 = pygame.font.Font("bin/fonts/ClearSans-Regular.ttf",20)
  winText = 'You Win!'
  loseText = 'You Lose!'
  replayText = 'Space: replay, ESC: exit'
  replay = font2.render(replayText,True,(0,0,0))
  messageText = ''
  
  if win == True:
    message = font.render(winText,True,(0,0,0))
    messageText = winText
  else:
    message = font.render(loseText,True,(0,0,0))
    messageText = loseText
  
  surface.blit(message,(rect.x + (rect.width/2)  - (font.size(messageText)[0]/2), 
                        rect.y + (rect.height/2) - (font.size(messageText)[1] + font2.size(replayText)[1])/2 + 3))
  surface.blit(replay, (rect.x + (rect.width/2)  - (font2.size(replayText)[0]/2) ,
                        rect.y + (rect.height/2) - (font.size(messageText)[1] + font2.size(replayText)[1])/2 + font.size(messageText)[1] - 3))
  
  pygame.display.update()


    
      
  


      



