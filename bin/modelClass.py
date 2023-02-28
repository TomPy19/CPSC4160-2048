from bin.cRectangle import cRectangle
import random
import math

# Size of each cell
rectSize = rectWidth, rectHeight = 100, 100

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
]

# Initialize empty gameboard
gameBoard = {}
score = {}

def startGame(gameBoard):
  # Initialize gameboard cells
  for x in range(4):
    gameBoard[x] = {}
    for y in range(4):
      gameBoard[x][y] = cRectangle(x, y, rectWidth, rectHeight, colors[0], 0)

  # Spawn two random cells to start the game with
  spawnRect(gameBoard)
  spawnRect(gameBoard)

  score['score']=0

# Function to spawn a random 2 or 4 in an empty cell
def spawnRect(gameBoard):
  # Obtain dict of all free spaces in gameboard
  notFull = checkFree(gameBoard)

  # Call random on dict of not full x spaces
  x = random.choice(list(notFull.keys()))

  
  if notFull[x]:
    y = random.choice(notFull[x]) # If x row exists, obtain random y from value pair
  else: # Just spawn in first entry of empty spaces
    y = notFull[0][0]

  # List of a 90% chance to spawn a 2 and a 10% chance to spawn a 4
  randSpawnList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
  value = random.choice(randSpawnList)

  gameBoard[x][y].color = colors[value+1] # Update color of cell
  gameBoard[x][y].value = (value+1)*2     # Update value of cell
  
# Function to return dict of all empty cells on the board
def checkFree(gameBoard):
  # Initalize new dict
  freeSpace = {}

  # Append all cells that are of value zero
  for x in range(4):
    list = []
    for y in range(4):
      if gameBoard[x][y].value == 0:
        list.append(y)
    if len(list) > 0:
      freeSpace.update({x: list})

  return freeSpace

# Function to return if there are no empty cells on the board
def checkFull(gameBoard):
  for x in range(4):
    for y in range(4):
      if gameBoard[x][y].value == 0:
        return False
  return True

# Function to check if any cells can still be merged, even if board is full
def checkLose(gameBoard, dir):
  for x in range(4):
    for y in range(4):
      c1 = gameBoard[x][y]
      c2 = getC2(dir, gameBoard, x, y)
      if c2:
        if c1.value == c2.value:
          return False
  return True

# Function to check if 2048 exists on the gameboard
def checkWin(gameBoard):
  for x in range(4):
    for y in range(4):
      if gameBoard[x][y].value == 2048:
        return True
  return False

# Function to move the cells in the direction of the input
def moveBoard(dir, gameBoard, moveList, it):
  if dir == 'r':
    return moveRight(gameBoard, moveList, it)
  if dir == 'l':
    return moveLeft(gameBoard, moveList, it)
  if dir == 'u':
    return moveUp(gameBoard, moveList, it)
  if dir == 'd':
    return moveDown(gameBoard, moveList, it)

# Function to merge all adjacent cells of same value
def mergeDir(dir, gameBoard, score):
  merged = False
  if dir == 'l' or dir == 'u':
    for x in range(0,4):
      for y in range(0,4):
        if merge(dir, gameBoard, x, y, score):
          merged = True
  elif dir == 'r' or dir == 'd':
    for x in range(3,-1,-1):
      for y in range(3,-1,-1):
        if merge(dir, gameBoard, x, y, score):
          merged = True
  return merged

# Helper function to merge based off of the input direction
def merge(dir, gameBoard, x, y, score):
  merged = False
  if dir == 'l' or dir == 'u':
    c1 = gameBoard[x][y]
    c2 = getC2(dir, gameBoard, x, y)
  elif dir == 'r' or dir == 'd':
    c2 = gameBoard[x][y]
    c1 = getC2(dir, gameBoard, x, y)
  if c1 and c2:
    if c1.value != 0 and c2.value != 0:
      if c1.value == c2.value:
        color_index = int(math.log2(c2.value)+1)
        gameBoard[(c2.rect.x-20)/120][(c2.rect.y-120)/120].color = colors[color_index]
        c2.value*=2
        c1.value = 0
        c1.color = colors[0]
        incrementDir(dir, x, y)
        merged = True
        score['score'] = score['score']+c2.value
  return merged

# Function to return the next cell to check in given direction
def getC2(dir, gameBoard, x, y):
  try:
    if dir == 'r' or dir == 'l':
      return gameBoard[x-1][y]
    if dir == 'u' or dir == 'd':
      return gameBoard[x][y-1]
  except:
    return None
  
# Function to increment x or y by one after a merge
def incrementDir(dir, x, y):
  if dir == 'l' or dir == 'r':
    x+=1
  if dir == 'u' or dir == 'd':
    y+=1
  
# Function to call all helper functions after a direction is pressed
def handleKeypress(dir, gameBoard, score):
  # Iterator to check if data of moves should be stored
  it = 1
  # List of changes made by move function
  listMoves = {}
  moveBoard(dir, gameBoard, listMoves, it)
  merged = mergeDir(dir, gameBoard, score)
  it-=1
  moveBoard(dir, gameBoard, listMoves, it)
  # Only spawn new cell if board moves or a merge happens
  if listMoves or merged: spawnRect(gameBoard)
  return listMoves

# Function to shift entire board right
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

# Function to shift entire board left
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
          dest = x-zeros
          if dest < 0:
            moveList[f'{len(moveList)}'] = {'l': [gameBoard[x][y], gameBoard[0][y]]}
          else:
            moveList[f'{len(moveList)}'] = {'l': [gameBoard[x][y], gameBoard[dest][y]]}
    for x in range(4):
      gameBoard[x][y].value = arr[x]
      if arr[x] == 0:
        gameBoard[x][y].color = colors[0]
      else:
        gameBoard[x][y].color = colors[int(math.log2(arr[x]))]
  return gameBoard

# Function to shift entire board up
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
          dest = y-zeros
          if dest < 0:
            moveList[f'{len(moveList)}'] = {'u': [gameBoard[x][y], gameBoard[x][0]]}
          else:
            moveList[f'{len(moveList)}'] = {'u': [gameBoard[x][y], gameBoard[x][dest]]}
    for y in range(4):
      gameBoard[x][y].value = arr[y]
      if arr[y] == 0:
        gameBoard[x][y].color = colors[0]
      else:
        gameBoard[x][y].color = colors[int(math.log2(arr[y]))]
  return gameBoard

# Function to shift entire board down
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
