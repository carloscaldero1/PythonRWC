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
elif overallAvgScore >= 70 and overallAvgScore <= 74:
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




