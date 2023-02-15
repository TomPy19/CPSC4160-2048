import pygame

rectSize = rectWidth, rectHeight = 100, 100
rectPos = rectX, rectY = 100, 100

# Number Colors
color_2 = (240,228,217)
color_4 = (236,224,200)
color_8 = (242,177,121)
color_16 = (245,149,99)
color_32 = (245,124,95)
color_64 = (245,124,95)
color_128 = (237,206,113)
color_256 = (237,205,96)
color_512 = (236,200,80)
color_1024 = (237,197,63)
color_2048 = (238,194,46)
color_max = (61,58,51)

gameBoard = {}

for x in range(4):
  gameBoard[x] = {}
  for y in range(4):
    gameBoard[x][y] = (pygame.Rect(20+(x*120), 120+(y*120), rectWidth, rectHeight))