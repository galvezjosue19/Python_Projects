#The secret word the player is trying to guess
secretWord = "CBTNuggets"
lettersGuessed = ""

#The number of turns befoer the player Loses
failureCount = 6

#Loop until the player has made too many failed attempts
#Will 'break' the loop if they succeed instead
while failureCount > 0:
   
    #Get the guessed letter from the player
   guess = input("Enter a letter: ")

   if guess in secretWord:
      #Player guessed a correct letter!
      print(f"Correct! There is one or more {guess} in the secret word.") 
   else:
      failureCount -= 1
      print(f"Incorrect! There are no{guess} in the secret word. {failureCount} turns left.")