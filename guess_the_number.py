import random

# setting the minimum, maximum, and number of guesses
min = 1
max = 10
numGuesses = 5

# picking the number
number = random.randrange(min, max+1)

# a helpful dictionary that translates yes and no to True and False
ui = {"y":True, "n":False, "Y":True, "N":False, "Yes":True, "No":False, "yes":True, "no":False}

# checks if the user wants hints
while True:
  try:
    hints = ui[input("Would you like hints (y/n)? ")]
    break
  except KeyError:
    print("That isn\'t a valid option")

# game
for x in range(1, numGuesses+1):
  print("---")
  print("This is try #"+str(x))
  print("I\'m thinking of a number between "+str(min)+" and "+str(max))

  # gets guess
  while True:
    try:
      guess = int(input("Your guess: "))
      if guess > max:
        int("a")
      elif guess < min:
        int("a")
      break
    except ValueError:
      print("Sorry, that\'s not a valid guess")

  # checks guess
  if guess == number:
    print("Congratulations! You've guessed the correct number!")
    break
  if hints:
    if guess > number:
      print("That\'s incorrect. My number is smaller than that.")
    elif guess < number:
      print("That\'s incorrect. My number is bigger than that.")
print("---\nMy number was "+str(number)+"!")