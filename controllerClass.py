import pygame

def new_rect():
  keys = pygame.key.get_pressed()
  if keys[pygame.K_SPACE]:
    return True
  else :
    return False

  # if keys[pygame.K_LEFT] and Rect.left > 0:
  #   return
  # if keys[pygame.K_RIGHT] and Rect.right < viewClass.SCREEN_WIDTH:
  #   return
  # if keys[pygame.K_UP] and Rect.top > 0:
  #   return
  # if keys[pygame.K_DOWN] and Rect.bottom < viewClass.SCREEN_HEIGHT:
  #   return