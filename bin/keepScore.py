# Open high score from file
file = open("./bin/highScore.txt", 'r')
highScore = int(file.readlines()[0])
file.close()

# Save high score to file
def saveScore(score):
  file = open("./bin/highScore.txt", 'w')
  if score['score'] <= highScore: # Store higher of the two scores
    file.write(str(highScore))
  else:
    file.write(str(score['score']))
  file.close()
