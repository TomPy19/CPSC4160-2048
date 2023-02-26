from cRectangle import cRectangle
import random

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
board_color = (210, 195, 179)

gameBoard = {}

for x in range(4):
  gameBoard[x] = {}
  for y in range(4):
    gameBoard[x][y] = cRectangle(x, y, rectWidth, rectHeight, board_color, 0)

def spawnRect(gameBoard):
  notFull = checkFree(gameBoard)

  x = random.choice(list(notFull.keys()))

  print(notFull)
  if notFull[x]:
    y = random.choice(notFull[x])
  else:
    y = notFull[0][0]

  print(f'{x}, {y}')

  gameBoard[x][y].color = color_2
  gameBoard[x][y].value = 2

  return gameBoard
  
   
def checkFree(gameBoard):
  freeSpace = {}

  for x in range(4):
    list = []
    for y in range(4):
      if gameBoard[x][y].value == 0:
        list.append(y)
    if len(list) > 0:
      freeSpace.update({x: list})

  return freeSpace

