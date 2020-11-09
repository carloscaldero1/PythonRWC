# This is a guess the number game.
#import random module 
import random

#Ask user to guess the number the computer is thinking of
#Display Instructions to User
print("Let's play a game")
print("I am thinking of a number from 1 to 20...")
print("I will give you 5 chances to guess it")
print("If you guess it correctly you win, if you exhaust all 5 guesses you lose")
print(" ")

#set a variable to hold random integer from the range 1-20
randomGeneratedNumber = random.randint(1,20)    #The 1 and 20 are inclusive

#set a counter of guesses taken to 0
guessesTaken = 0

#Also could have started counter at 5 and decremented it after every guess then set the while contion to while guess < 0
while guessesTaken < 5:        #Also could have done while guessTaken != 5
    print(" ")              #For formatting purposes
    userGuess = int(input("Take a guess: "))    #Ask for user input of guessed number and changes it to an integer 
    guessesTaken +=1     #Increments guesses taken by 1 
    #guessesTaken = guessesTaken +1 #same as line above

    if userGuess < randomGeneratedNumber:
        print("Your guess is too low, Try a higher number")  # too low Hint
        continue
    elif userGuess > randomGeneratedNumber:
        print("Your guess is too high, Try a lower number")   #too high Hint
        continue
    elif userGuess == randomGeneratedNumber:         #Also could haved done it this way
        break 
   # else:                                             #Because the only other logical option there is, is for it to be equal
    #    break
    
#The section Below will execute only when the while condition is no longer true and the loop is broken
#Or a section of the code was true and it hit a break statement
print(" ")            #For formatting purposes


if userGuess == randomGeneratedNumber:                      
   print("Yes! You Win! " + str(randomGeneratedNumber) + " is the exact number I was thinking of!")   #executes if number was right
    
else:
    print("Sorry,You Lose. The number I was thinking of was " + str(randomGeneratedNumber)+ ".")        #executes if ran out of guesses








