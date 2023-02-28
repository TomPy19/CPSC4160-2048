file = open("./bin/highScore.txt", 'r')
highScore = int(file.readlines()[0])
file.close()

def saveScore(score):
  file = open("./bin/highScore.txt", 'w')
  if score['score'] <= highScore:
    file.write(str(highScore))
  else:
    file.write(str(score['score']))
  file.close()
