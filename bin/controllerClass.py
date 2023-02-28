import pygame

# Function to return which direction is being pressed in arrow keys
def controls(event):
  keys = pygame.key.get_pressed()
  if event.type == pygame.KEYDOWN:
    if keys[pygame.K_LEFT]:
      return 'l'
    elif keys[pygame.K_RIGHT]:
      return 'r'
    elif keys[pygame.K_UP]:
      return 'u'
    elif keys[pygame.K_DOWN]:
      return 'd'
  else:
    return None

# Function to return if space or esc is pressed after game end
def getDecision():
  keys = pygame.key.get_pressed()
  if keys[pygame.K_SPACE]:
    return 'space'
  elif keys[pygame.K_ESCAPE]:
    return 'esc'
  else:
    return None

# Function to check if the directional keypress should move the board
def shouldRun(state, dir):
  if dir == 'l':
    key = pygame.key.get_pressed()[pygame.K_LEFT]
  elif dir == 'r':
    key = pygame.key.get_pressed()[pygame.K_RIGHT]
  elif dir == 'u':
    key = pygame.key.get_pressed()[pygame.K_UP]
  elif dir == 'd':
    key = pygame.key.get_pressed()[pygame.K_DOWN]
  else:
    return False

  # Logic gate only returning true if the code has not already 
  # run and key is being pressed
  if state and key:
    return False
  elif not state and key:
    return True
  elif not state and not key:
    return False