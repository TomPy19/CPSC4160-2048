from cRectangle import cRectangle
import random
import math

rectSize = rectWidth, rectHeight = 100, 100
rectPos = rectX, rectY = 100, 100

# Number Colors
colors = [
  (210,195,179), # 0
  (240,228,217), # 2
  (236,224,200), # 4
  (242,177,121), # 8
  (245,149,99),  # 16
  (245,124,95),  # 32
  (246,93,59),   # 64
  (237,206,113), # 128
  (237,205,96),  # 256
  (236,200,80),  # 512
  (237,197,63),  # 1024
  (238,194,46),  # 2048
  (61,58,51)     # max
]

gameBoard = {}

def spawnRect(gameBoard):
  notFull = checkFree(gameBoard)

  x = random.choice(list(notFull.keys()))

  # print(notFull)
  if notFull[x]:
    y = random.choice(notFull[x])
  else:
    y = notFull[0][0]

  # print(f'{x}, {y}')

  randSpawnList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
  value = random.choice(randSpawnList)
  gameBoard[x][y].color = colors[value+1]
  gameBoard[x][y].value = (value+1)*2

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

for x in range(4):
  gameBoard[x] = {}
  for y in range(4):
    gameBoard[x][y] = cRectangle(x, y, rectWidth, rectHeight, colors[0], 0)
spawnRect(gameBoard)
spawnRect(gameBoard)

def moveBoard(dir, gameBoard, moveList, it):
  if dir == 'r':
    return moveRight(gameBoard, moveList, it)
  if dir == 'l':
    return moveLeft(gameBoard, moveList, it)
  if dir == 'u':
    return moveUp(gameBoard, moveList, it)
  if dir == 'd':
    return moveDown(gameBoard, moveList, it)

def mergeDir(dir, gameBoard):
  # print(gameBoard)
  for x in range(4):
    for y in range(4):
      c1 = gameBoard[x][y]
      c2 = getC2(dir, gameBoard, x, y)
      if c2:
        if c1.value == c2.value:
          if c2.value != 0:
            color_index = int(math.log2(c2.value)+1)
          else:
            color_index = 1
          if color_index > len(colors):
            gameBoard[(c2.rect.x-20)/120][(c2.rect.y-120)/120].color = colors[len(colors) - 1]
          else:
            gameBoard[(c2.rect.x-20)/120][(c2.rect.y-120)/120].color = colors[color_index]
          c2.value*=2
          c1.value = 0
          c1.color = colors[0]
        incrementDir(dir, x, y)
  return gameBoard

def getC2(dir, gameBoard, x, y):
  try:
    if dir == 'r':
      return gameBoard[x+1][y]
    if dir == 'l':
      return gameBoard[x-1][y]
    if dir == 'u':
      return gameBoard[x][y-1]
    if dir == 'd':
      return gameBoard[x][y+1]
  except:
    return None
  
def incrementDir(dir, x, y):
  if dir == 'l' or dir == 'r':
    x+=1
  if dir == 'u' or dir == 'd':
    y+=1
  
def handleKeypress(dir, gameBoard):
  it = 1
  listMoves = {}
  moveBoard(dir, gameBoard, listMoves, it)
  mergeDir(dir, gameBoard)
  it-=1
  moveBoard(dir, gameBoard, listMoves, it)
  if listMoves: gameBoard = spawnRect(gameBoard)
  return listMoves

def moveRight(gameBoard, moveList, it):
  for y in range(4):
    zeros = 0
    arr = []
    for x in range(4):
      arr.append(gameBoard[x][y].value)
    for x in range(4):
      if arr[x] == 0:
        del arr[x]
        arr.insert(0,0)
        zeros+=1
    if it:
      for x in range(4):
        if gameBoard[x][y].value != arr[x]:
          dest = x+zeros
          if dest > 3:
            moveList[f'{len(moveList)}'] = {'r': [gameBoard[x][y], gameBoard[3][y]]}
          else:
            moveList[f'{len(moveList)}'] = {'r': [gameBoard[x][y], gameBoard[dest][y]]}
    for x in range(4):
      gameBoard[x][y].value = arr[x]
      if arr[x] == 0:
        gameBoard[x][y].color = colors[0]
      else:
        gameBoard[x][y].color = colors[int(math.log2(arr[x]))]
  return gameBoard

def moveLeft(gameBoard, moveList, it):
  for y in range(4):
    zeros = 0
    arr = []
    for x in range(4):
      arr.append(gameBoard[x][y].value)
    for x in range(4):
      if arr[x] == 0:
        del arr[x]
        arr.append(0)
        zeros+=1
    if it:
      for x in range(4):
        if gameBoard[x][y].value != arr[x]:
          dest = x+zeros
          if dest > 3:
            moveList[f'{len(moveList)}'] = {'l': [gameBoard[x][y], gameBoard[3][y]]}
          else:
            moveList[f'{len(moveList)}'] = {'l': [gameBoard[x][y], gameBoard[dest][y]]}
    for x in range(4):
      gameBoard[x][y].value = arr[x]
      if arr[x] == 0:
        gameBoard[x][y].color = colors[0]
      else:
        gameBoard[x][y].color = colors[int(math.log2(arr[x]))]
  return gameBoard

def moveUp(gameBoard, moveList, it):
  for x in range(4):
    zeros = 0
    arr = []
    for y in range(4):
      arr.append(gameBoard[x][y].value)
    for y in range(4):
      if arr[y] == 0:
        del arr[y]
        arr.append(0)
        zeros+=1
    if it:
      for y in range(4):
        if gameBoard[x][y].value != arr[y]:
          dest = y+zeros
          if dest > 3:
            moveList[f'{len(moveList)}'] = {'u': [gameBoard[x][y], gameBoard[x][3]]}
          else:
            moveList[f'{len(moveList)}'] = {'u': [gameBoard[x][y], gameBoard[x][dest]]}
    for y in range(4):
      gameBoard[x][y].value = arr[y]
      if arr[y] == 0:
        gameBoard[x][y].color = colors[0]
      else:
        gameBoard[x][y].color = colors[int(math.log2(arr[y]))]
  return gameBoard

def moveDown(gameBoard, moveList, it):
  for x in range(4):
    zeros = 0
    arr = []
    for y in range(4):
      arr.append(gameBoard[x][y].value)
    for y in range(4):
      if arr[y] == 0:
        del arr[y]
        arr.insert(0,0)
        zeros+=1
    if it:
      for y in range(4):
        if gameBoard[x][y].value != arr[y]:
          dest = y+zeros
          if dest > 3:
            moveList[f'{len(moveList)}'] = {'d': [gameBoard[x][y], gameBoard[x][3]]}
          else:
            moveList[f'{len(moveList)}'] = {'d': [gameBoard[x][y], gameBoard[x][dest]]}
    for y in range(4):
      gameBoard[x][y].value = arr[y]
      if arr[y] == 0:
        gameBoard[x][y].color = colors[0]
      else:
        gameBoard[x][y].color = colors[int(math.log2(arr[y]))]
  return gameBoard