#Final Project

def menuReturnQuestion():
    while True:
        print(" ")
        print("Would you like to return to the main menu?")
        restartOption = input("Enter YES(all caps) to return or NO(all caps) to exit: ")
        print(" ")
        if restartOption == 'YES':
            mainMenu()
            break
        elif restartOption == 'NO':
            print("Exiting Now....")
            exit()
            break
        else:
            print("You have entered an invaild option(be sure to enter all caps) ")
            continue
#_________________________________________________________________________________________________________________________________
def registerAccount():
    #paste acct Reg code here #WHEN PASTING BE SURE TO INDENT ACCORDING TO FUNCTION SYNTAX A QUICK WAY IS TO HIGLIGHT AND SHIFT+TAB on Python IDLE and HIGHLIGHT+TAB ON REPL shift+tab on repl is to untab
     
    print(" \t \t Register an Account")

    #Display Username and password Requirements for user to register an account

    print("\n")
    print("A Username must meet these requirements: ")
    print("-Atleast 8 characters long")
    print("-Must end with a number")
    print("\n")
    print("A Strong password consists of these requirements:")
    print("-Atleast 10 total characters")
    print("-Must start with a captital letter")
    print("-Must end with a special character(from this list:!@#$%*&)")
    print("\n")

    #Alterantive Way to print everything above in fewer lines
    '''
    print("\n")
    print("A Username must meet these requirements: \n-Atleast 8 characters long \n-Must end with a number")
    print("\n")
    print("A Strong password consists of these requirements: \n-Atleast 10 total characters \n-Must start with a captital letter \n-Must end with a special character(from this list:!@#$%*&)")
    print("\n")
    '''
    #Defining variables to satisfy conditons below, I did this part last!!!
    specialChar = "!@#$%*&"
    capLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    nums = "0123456789"

    #This section of the code will now ask the user to input their desired Username and Password
    #If it is invalid it will ask them to enter it again

    while True:
        userName = input("Enter a valid username: ")
        if len(userName) < 8: 
            print("This username is invalid because it is shorter than 8 characters") #Invalid message
            print(" ")
            continue # to make user go back to input line
        elif userName[-1] not in nums:
            print("This username is invalid because it does not end with a number") #Invalid message
            print(" ")
            continue # to make user go back to input line    
        else:
            break
           
    print("Username Accpted")
    print("\n") # to skip a line for formatting purposes

    while True:
        passWord = input("Enter a vaild password: ")
        if len(passWord) < 10:                 # or password not in aplhaNumericCollection or password[0] not in capLetters:
            print("This is an invalid password, because it is shorter than 10 characters")#Invalid message
            print(" ")
            continue # to make user go back to input line
        elif passWord[0] not in capLetters:
            print("This is an invalid password, because it is does not begin with a Capital Letter")#Invalid message
            print(" ")
            continue # to make user go back to input line
        elif passWord[-1] not in specialChar:
            print("This is an invalid password, because it is does not end with a special Character")#Invalid message
            print(" ")
            continue # to make user go back to input line
        else:
            break

    print("Password Accepted")
    print("\n") # to skip a line for formatting purposes


    #This section of the program will display a success message and credentials if they are valid
    print("Account has been successfully registered, your credentials are: ")
    print("UserName: " + userName)
    print("Password: " + passWord)

    #Call mainMenu function to retrive main menu again AUTOMATICALLY
    #mainMenu()

    #Call the menuReturnQuestion to give the user the option to return to the menu or to exit
    menuReturnQuestion()
#___________________________________________________________________________________________________________________________________
#Data Entry function
def dataEntry():
    #This Program will take user input and will output all of that information

    firstName = input("Enter First Name: ")         #Takes String Input
    lastName = input("Enter Last Name: ")           #Takes String Input
    birthDay = input("Enter Date of Birth: ")       #Takes String Input
    age = int(input("Enter Age: "))                 #Takes int Input
    eyeColor = input("Enter Eye Color: ")           #Takes String Input
    feet = int(input("Enter height in feet: "))     #Takes int Input
    inches = int(input("Enter height in inches: ")) #Takes int Input
    homeTown= input("Enter Home Town: ")            #Takes String Input


    print(" ")                                      #For formatting purposes, to seperate Input from output 
    print(" \t \t Data Entry Report")                      #'\t' Makes a tab in a string so I tabbed over twice for formatting purposes  
    print("Name: " + firstName + " " + lastName)    #Space is to seperate Firstname from last name for formatting purposes, also could have added whitespace in input format above
    print("Date of Birth: " + birthDay)
    print("Age: " + str(age))
    print("Eye Color: "+ eyeColor)
    print("Height: " + str(feet) + "'" + str(inches) + '"') #Notice The " and ' format, becareful to not confuse the intrepreter 
    print("Home Town : " + homeTown)

    #Call mainMenu function to retrive main menu again AUTOMATICALLY
    #mainMenu()

    #Call the menuReturnQuestion to give the user the option to return to the menu or to exit
    menuReturnQuestion()
#____________________________________________________________________________________________________________________________________
#Progress Report function
def progressReport():
    #paste progress report here
    print(" \t \t Progress Report")                     #\t is to tab over and try to center output for formatting purposes

    mathScore = int(input("Enter your current math score: "))   # integer input
    print(" ")                                  #To skip a line, for formatting purposes
    scienceScore = int(input("Enter Your current science score: ")) # integer input
    print(" ")                                  #To skip a line, for formatting purposes
    englishScore = int(input("Enter Your current english score: ")) # integer input
    print(" ")                                  #To skip a line, for formatting purposes
    historyScore = int(input("Enter Your current history score: ")) # integer input
    print(" ")                                  #To skip a line, for formatting purposes


    overallAvgScore = (mathScore + scienceScore + englishScore + historyScore)/4  #Averages the overall score of all classes
    #overallAvgScore = int((mathScore + scienceScore + englishScore + historyScore)/4)   #if I wanted to display as and integer instead of a float
    print ("Your current overall Score is: " + str(overallAvgScore))               # Prints overall score and converts to a str in order to do so                
    #If-else block for every possible outcome A,B+,B,C+,C,D,Or F
    if overallAvgScore >= 90:                                   
        overallLetterGrade = "A"  
    elif overallAvgScore >= 85 and overallAvgScore <= 89:
        overallLetterGrade = "B+"
    elif overallAvgScore >= 80 and overallAvgScore <= 84:
        overallLetterGrade = "B"
    elif overallAvgScore >= 75 and overallAvgScore <= 79:
        overallLetterGrade = "C+"
    elif overallAvgScore >= 70 and overallAvgScore <= 75:
        overallLetterGrade = "C"
    elif overallAvgScore >= 65 and overallAvgScore <= 69:
        overallLetterGrade = "D"
    else:
        overallLetterGrade = "F"                            #If overallAvgScore is not true for any other the if statements above then it must below 65 which is an a F
        
        
    print("Your current overall letter grade is: " + overallLetterGrade)     #prints the letter grade which is true above

    if overallLetterGrade == "A" or overallLetterGrade == "B+" or overallLetterGrade == "B":   #Compares overallLetterGrade to Strings A, B+, B.. if it is is one of those it will print that message
        print ("You are doing great, Keep up the good work!!")
    elif overallLetterGrade == "C" or overallLetterGrade == "C+":                                #Same as above excpet doing comparison for C OR C+
        print ("You are doing ok, but you need to study a little more")
    else:
        print ("You are not doing well, you need to study a lot more")                      #If it is not A-C+ it means that by process of elimination all that's left is D and F so it will print that respective message

    #Call mainMenu function to retrive main menu again AUTOMATICALLY
    #mainMenu()

    #Call the menuReturnQuestion to give the user the option to return to the menu or to exit
    menuReturnQuestion()
#____________________________________________________________________________________________________________________________________
#Number guessing game function
def numberGuessGame():
    #paste number guessing game code here
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
        #elif userGuess == randomGeneratedNumber:         #Also could haved done it this way
         #   break 
        else:                                             #Because the only other logical option there is, is for it to be equal
            break
    #The section Below will execute only when the while condition is no longer true and the loop is broken
    #Or a section of the code was true and it hit a break statement
    print(" ")            #For formatting purposes
    if userGuess == randomGeneratedNumber:                      
        print("Yes! You Win! " + str(randomGeneratedNumber) + " is the exact number I was thinking of!")   #executes if number was right
        
    else:
        print("Sorry,You Lose. The number I was thinking of was " + str(randomGeneratedNumber)+ ".")        #executes if ran out of guesses

    #Call mainMenu function to retrive main menu again AUTOMATICALLY
    #mainMenu()

    #Call the menuReturnQuestion to give the user the option to return to the menu or to exit
    menuReturnQuestion()
#_____________________________________________________________________________________________________________________________________
#Turtle function
def turtleArt():
    import time 
    import turtle
    screen = turtle.Screen()
    t = turtle.Turtle()
    t.width(5)
    #paste turtle code here
    #Shape Functions
    #Actually did this part last
    def drawSquare():
        for i in range(4):
            t.fd(100)
            t.rt(90) #or t.fd(360/4)
        time.sleep(2)
        t.clear()
        #screen.exitonclick()  #To exit turtle screen just click on it
    def drawTriangle():
        for i in range(3):
            t.fd(100)
            t.lt(120) #or t.fd(360/3)
        time.sleep(2)
        t.clear()
    def drawCircle():
        t.circle(100)
        time.sleep(2)
        t.clear()
    def drawHexagon():
        for i in range(6):
            t.fd(100)  
            t.rt(60) #or t.fd(360/6)
        time.sleep(2)
        t.clear()
              
    def drawOctagon():
        t.width(5)
        for i in range(8):
            t.fd(100)  
            t.rt(45) #or t.fd(360/8)
        time.sleep(2)
        t.clear()
         
    shapeList = ['square', 'triangle', 'circle', 'hexagon','octagon']
    print("I can draw shapes")
    print("I can draw a square, a triangle, a circle, a hexagon, or an octagon")
    print(" ")

    while True:
        shapeEntered = input("What shape would you like to see? (must be all lowercase) ")
        if shapeEntered not in shapeList:
            print("You entered an invalid shape or misspelled it, do not forget it has to be all lowercase")
            print(" ")
            continue
        else:
            print(" ")
            print("Open Turtle Window to view drawing")
            break
    print("TURTLE DRAWING WILL ONLY LIVE FOR 2 SECONDS. THEN SCREEN WILL CLEAR")
    if shapeEntered == 'square':
        drawSquare()
        #print("square") #for testing purposes before actually defining functions
    elif shapeEntered == 'triangle':
        drawTriangle()
        '''import turtle
        screen = turtle.Screen()  #Could also put turtle inside function!! Will pop up in window when conditional above is true
        t = turtle.Turtle()'''
        #print("triangle") #for testing purposes before actually defining functions
    elif shapeEntered == 'circle':
        drawCircle()
        #print("circle") #for testing purposes before actually defining functions
    elif shapeEntered == 'hexagon':
        drawHexagon()
        #print("Hexagon") #for testing purposes before actually defining functions
    else:
        drawOctagon()
        #print("Octagon") #for testing purposes before actually defining functions

    print(" ")
    
    #Call mainMenu function to retrive main menu again AUTOMATICALLY
    #mainMenu()

    #Call the menuReturnQuestion to give the user the option to return to the menu or to exit
    menuReturnQuestion()


#_______________________________________________________________________________________________________________________________________
    

#Where Program Output actually starts
#Greeting
userName = input("Hello, What is your name? ")
print(" ")
print("Welcome " + userName +" See the Menu below")
print(" ")

#Def this function as mainMenu and call this function at the end of every program to return to menu
def mainMenu():
    import time
    print(" ")
    print("Opening Menu..........")
    print(" ")
    time.sleep(1)
    print("\t \t Menu")

    #print menu options

    print("Enter 1 to register account.")
    print("Enter 2 for Data Entry.")
    print("Enter 3 for Progress Report.")
    print("Enter 4 to play number guessing game.")
    print("Enter 5 to see Turtle Art.")
    print("Enter 'Exit' or anything other key to end and exit the program.")
    print(" ")
    #ask for user input and save as variable 
    userChoice = input("Choose an option above by entering the corresponding key: ")
    print(" ")


    if userChoice == '1':           #As string so user can not break program with in valid data type as response for userChoice input
        registerAccount()
        #print(" acct reg")         #For testing purposes
    elif userChoice == "2":
        dataEntry()
        #print("data entry")        #For testing purposes
    elif userChoice == "3":
        progressReport()
        #print("progress report")   #For testing purposes
    elif userChoice == "4":
        numberGuessGame()
        #print("num guess game")    #For testing purposes
    elif userChoice == "5":
        turtleArt()
        #print("turtle")             #For testing purposes
    else:
        print("Exiting Now......")      #exiting message
        time.sleep(1)
        print("Good Bye!")
        time.sleep(1)
        exit()                          #exit function
        

#Call mainMenu function for the first time in the program output
mainMenu()







    
