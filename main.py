import random
import time

highScore = 0
timesPlayed = 0

def startDialogue():
  print("Alright lets play a little game.")
  time.sleep(2)
  print("How about you guess what number I am thining of.")
  time.sleep(2)
  print("It would take way too long though if it can be any number though.")
  time.sleep(2)

def lowNumber():
  print("So what should the lowest number I can pick be?")
  global startRange
  while True:
    startRange = input("")
    if startRange.isalpha():
      print("Please enter a number.")
    else:
      startRange = int(startRange)
      break

def highNumber():
  print("Alright what is the highest number that I can pick?")
  global endRange
  while True:
    endRange = input("")
    if endRange.isalpha():
      print("Please enter a number.")
    else:
      endRange = int(endRange)
      break

def testRange():
  while True:
    if endRange <= startRange:
      print("Sorry but the end number has to be bigger then the start number.")
      print("That means we have to change one of them.")
      print("Would you like to change the start number? (Yes/No)")
      while True:
        check = input(" ").lower()
        if check == "yes":
          lowNumber()
          break
        elif check == "no":
          print("Then lets change the end number.")
          highNumber()
          break
        else:
          print("It has to be Yes or No")
    else:
      break

def guess():
  print("Alright let's give it a go.")
  time.sleep(2)
  
  global guessCount
  guessCount = 0
  while True:
    guess = int(input("Guess: "))
    guessCount = guessCount + 1
    if guess == answer and guessCount <= 1:
      print("You guessed it first try!!! There is no way anyone is beating that high score.")
      time.sleep(2)
      print("Someone is probably cheating. ;) ")
      break
    elif guess == answer and guessCount > 1:
      print("Well look at that you finally got it!")
      break
    elif guess > answer:
      print("It's lower then that.")
      continue
    elif guess < answer:
      print("It's higher then that.")
      continue
    else:
      continue

def scoring():
  print("I told you I was keeping score and I was, so let's see how you did.")
  time.sleep(2)

  if highScore == finalScore:
    print("Well look at that, it seems you set the highscore with a score of: " + str(highScore))
    time.sleep(2)
    print("This is probably just the first time someone has played it though so I hope you don't feel that special.")
  else:
    print("Looks like you didn't set any records today did ya.")
    time.sleep(2)
    print("The high score is: " + str(highScore))
    time.sleep(2)
    print("That rough for you buddy because your score was only " + str(finalScore))
    time.sleep(2)
    print("Ouch so close. But not really though.")
    time.sleep(2)

startDialogue()
while True:
  lowNumber()
  highNumber()
  testRange()
  numbers = range(startRange,endRange)
  answer = random.choice(numbers)
  if timesPlayed == 0:
    print("Everytime you get it wrong I'll even give you a hint to help you out. ;) ")
    time.sleep(2)
    print("But the more guesses that it takes the lower your score will be because I am keeping track.")
    time.sleep(2)
  guess()
  global finalScore
  finalScore = 1000 * (1 - (guessCount / endRange)) 
  if finalScore > highScore:
    highScore = finalScore
  else:
    highScore = highScore
  scoring()
  print("Well that's about it.")
  while True:
    continuePlaying = input("Do you want to play again to beat that lame score you got? (Yes/No) ").lower()
    if continuePlaying == "yes":
      print("Sounds good let's go again.")
      timesPlayed = timesPlayed + 1
      break
    elif continuePlaying == "no":
      print("Well looks like this is goodbye then :) ")
      break
    else:
      print("It has to be a Yes or No")
  if continuePlaying == "no":  
    break
  else:
    continue