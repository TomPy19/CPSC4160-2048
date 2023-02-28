import pygame

class cRectangle:
    def __init__(self, x, y, width, height, color, value):
        self.rect = pygame.Rect(20+(x*120), 120+(y*120), width, height)
        self.color = color
        self.value = value
