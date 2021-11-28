# Program 2: Password validator
# Create a program that check if password is valid
# The password is valid if all criteria are met:
# a. Greater than 15 letters
# b. Have at least one capital letter
# c. Have at least one number
# d. Have at least one special char

import string

def validatePass(password):
    for char in password:
        if len(password) > 15:
            global length
            length = True
        if char.isupper():
            global capLettersNum 
            capLettersNum += 1
        if char.isnumeric():
            global numbersNum 
            numbersNum += 1
        if char in set(string.punctuation):
            global specialChar 
            specialChar += 1
       
def askPass():
    userPassword = input("Enter Password: ")
    validatePass(userPassword)
    global length
    global capLettersNum
    global numbersNum
    global specialChar 
    if length == True and capLettersNum > 0 and numbersNum > 0 and specialChar > 0:
        print("Password is Valid.")
    else:
        print("Password is Invalid. Please Try again.")
        askPass()

length = False
capLettersNum = 0
numbersNum = 0
specialChar = 0

askPass()
