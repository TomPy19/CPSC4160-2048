### The Game Document (README)
**Game Image:**





















**Program Versions**

OS Version: Windows 10, MacOS M1 Ventura 13.2

Python Version: 3.11.1

Pygame Version: 2.1.3

**Motivation:** We chose this game because we wanted more of a challenge and believed that 2048 would be a tougher implementation than pong. Since the project is an intro to game engine, we also felt that 2048 aligned with this because it is less graphically inclined. Therefore, we were able to put more time into the mechanics of the game. 

**Reasoning:** Our game's core is having a gameboard of "tiles'' which can be manipulated. With respect to this, we created a cRectangle class that contains a Pygame.rect object, color, and value variables. Our game board, an array of cRectangles, is designed this way so that we are able to assign/manipulate values and colors of the tiles when certain events happen.



**Image**:

**Future Work**:

Game engine wise, the game loop became a bit cluttered with various other logic, so possibly finding another way to refine it and have more abstraction would be a consideration. As far as new features are concerned, there are not many additional ones that could be added since 2048 is so bare bones. However, implementing some animations and further polishing the already miniscule amount of graphics of the game is a possible path. 

**Generalization**: Our game loop is generalizable enough that, with minor modifications, should be able to work for most simple games. It contains an initial game state, score tracker and in the event loop, it checks for win/loss, key presses, and displays the game. 
### Game Components
**Deviations:**

**Entities (Things)**: 

**Player Character**: Instead of a player character, It is more so that the player controls the board and moves the objects of the game board.

