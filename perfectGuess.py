import random
randnumber = random.randint(1, 100)
#print(randnumber)
userguess = None
guesses = 0

while(userguess != randnumber):
  userguess = int(input("Guess a number :\n"))
  guesses += 1
  if(userguess == randnumber):
    print("You guessed it right")
  elif(userguess > randnumber):
    print("You guessed it wrong! Enter a smaller number: ")
  elif(userguess<randnumber):
    print("You guessed it wrong! Enter a larger number: ")

print(f"You guessed the number in {guesses} guesses")