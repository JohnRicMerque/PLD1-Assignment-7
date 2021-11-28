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
    letterNum = 0
    capLettersNum = 0
    numbersNum = 0
    specialChar = 0
    for char in password:
        if char.isalpha():
            letterNum += 1
        if char.isupper(): 
            capLettersNum += 1
        if char.isnumeric(): 
            numbersNum += 1
        if char in set(string.punctuation): 
            specialChar += 1
    return letterNum, capLettersNum, numbersNum, specialChar

# Asks user input, validates and declares validation
def askPassValidate():
    while True:
        userPassword = input("Enter Password: ")
        letterG, capG, numG, specialG = validatePass(userPassword)
        # conditions 
        if letterG > 15 and capG > 0 and numG > 0 and specialG > 0:
            print("Password is Valid.")
            break
        if letterG <= 15:
            print("Invalid. Please include greater than 15 letters")
        if capG == 0:
            print("Invalid. Please include at least one capital letter")
        if numG == 0:
            print("Invalid. Please include at least one number")
        if specialG == 0:
            print("Invalid. Please include at least one special character")
        continue
    
# declaring the function
askPassValidate()
