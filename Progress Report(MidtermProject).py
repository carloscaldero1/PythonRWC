#SECTION 1: This section of the program is asking for the user input, which then is stored as information for later. The input that it is asking for is the 4 scores for the users school classes. The "int" keyword converts the  string input to an integer for future use and/or manipulation. The print "\n" lines create a spaced out new line for the output in between each statement

math_score = int(input("Enter Math Score: "))
print("\n")
science_score = int(input("Enter Science Score: "))
print("\n")
english_score = int(input("Enter English Score: "))
print("\n")
history_score = int(input("Enter History Score: "))
print("\n")

#SECTION 2: This line of the program is calculating the average of the inputs that the user entered, it takes the data and adds it all up and divides it by 4 which is the total number of classes that the user has in this scenario.

avg = (math_score + science_score + english_score+ history_score)/4
print("Your Overall Class Average Is: " + str(avg))
print("\n")

#SECTION 3: This section of the program is taking the averaged score that was previously defined and stored, and it compares them to a range of grade numbers to assign the corresponding grade letter for that averaged score. Therefore, an 'A' is anything above or equal to a 89.5.. a 'B+' is assigned if the averaged score is in between and 84.5 and an 89.4.. a 'B' would be anything between a 79.5 and an 84.4.....so on until it reaches the else statement which catches any other case that was not mentioned. Meaning if it is not an A,B+,B,C+,C,or D then it must be below 65 meaning that it is an 'F'. 

if avg >= 89.5:
  letter_grade = "A"
elif avg >= 84.5 and avg <= 89.4:
  letter_grade = "B+"
elif avg >= 79.5 and avg <= 84.4:
  letter_grade = "B"
elif avg >= 74.5 and avg <= 79.4:
  letter_grade = "C+" 
elif avg >= 69.5 and avg <= 74.4:
  letter_grade = "C"
elif avg >= 64.5 and avg <=69.4:
  letter_grade = "D"
else:
  letter_grade = "F"

#SECTION 4: This section of the program takes all the information, and writes it out in detailed sentences for the people to see. You will be able to see all the information thanks to this section. The \t \t characters are shortcut that makes it so that the words "Progress Report" are tabbed over twice which helps to keep them somewhat centered. The keyword "str" stands for string, the variables that hold the values for math,science,english, and history scores must be casted to a string to appear in the output. Otherwise this will return an error and crash the program. The last line of this section the program displyas the the letter grade that was defined above.  

print(" \t \t Progress Report")

print("Your Grade for Math is: " + str(math_score))

print("Your Grade for Science is: " + str(science_score))

print("Your Grade for English is: " + str(english_score))

print("Your Grade for History is: " + str(history_score))
print("\n")

print("Your Letter Grade is: " + letter_grade)

#SECTION 5: This section of the program displays a message to the user based on your values that were entered in the beginning of the program. This program will then compare the grade letter that you the user recieved with The coressponding message for that grade letter and display that message. In other words, it will say whether you did good, ok, or bad based on the information you gave it.

if letter_grade == "A" or letter_grade == "B+" or letter_grade == "B":
  print("You're doing great, keep up the good work!!")
elif letter_grade == "C+" or letter_grade == "C":
  print("You are doing ok, but you should study a little more")
else:
  print("You are performing very badly, you need to study a lot more")



