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
