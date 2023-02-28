import pygame

def controls(event):
  keys = pygame.key.get_pressed()
  if event.type == pygame.KEYDOWN:
    if keys[pygame.K_LEFT]:
      return 'l'
    if keys[pygame.K_RIGHT]:
      return 'r'
    if keys[pygame.K_UP]:
      return 'u'
    if keys[pygame.K_DOWN]:
      return 'd'
  else:
    return None

def shouldRun(state, dir):
  if dir == 'l':
    key = pygame.key.get_pressed()[pygame.K_LEFT]
  if dir == 'r':
    key = pygame.key.get_pressed()[pygame.K_RIGHT]
  if dir == 'u':
    key = pygame.key.get_pressed()[pygame.K_UP]
  if dir == 'd':
    key = pygame.key.get_pressed()[pygame.K_DOWN]
    
  if state and key:
    return False
  if not state and key:
    return True
  if not state and not key:
    return False
  