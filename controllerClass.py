import pygame

def controls(event):
  keys = pygame.key.get_pressed()
  if keys[pygame.K_SPACE] and (event.type == pygame.KEYDOWN):
    return True
  else:
    return False

def shouldRun(state):
  space = pygame.key.get_pressed()[pygame.K_SPACE]
  if state and space:
    return False
  if not state and space:
    return True
  if not state and not space:
    return False
  # if keys[pygame.K_LEFT] and Rect.left > 0:
  #   return
  # if keys[pygame.K_RIGHT] and Rect.right < viewClass.SCREEN_WIDTH:
  #   return
  # if keys[pygame.K_UP] and Rect.top > 0:
  #   return
  # if keys[pygame.K_DOWN] and Rect.bottom < viewClass.SCREEN_HEIGHT:
  #   return