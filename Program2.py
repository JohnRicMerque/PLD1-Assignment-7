# Program 2: Password validator
# Create a program that check if password is valid
# The password is valid if all criteria are met:
# a. Greater than 15 letters
# b. Have at least one capital letter
# c. Have at least one number
# d. Have at least one special char

import string

# looping characters and incrementing variables
def validatePass(password):
    length = False
    capLettersNum = 0
    numbersNum = 0
    specialChar = 0
    for char in password:
        if len(password) > 15:
            length = True
        if char.isupper(): 
            capLettersNum += 1
        if char.isnumeric(): 
            numbersNum += 1
        if char in set(string.punctuation): 
            specialChar += 1
    return length, capLettersNum, numbersNum, specialChar

# Asks user input, validates and declares validation
def askPassValidate():
    userPassword = input("Enter Password: ")
    lengthG, capG, numG, specialG = validatePass(userPassword)
    # conditions 
    if lengthG == True and capG > 0 and numG > 0 and specialG > 0:
        print("Password is Valid.")
    else:
        print("Password is Invalid. Please Try again.")
        askPassValidate()

# declaring the function
askPassValidate()
