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
        print("This username is invalid becasue it is shorter than 8 characters") #Invalid message
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








