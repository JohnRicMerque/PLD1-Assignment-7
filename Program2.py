# Program 2: Password validator
# Create a program that check if password is valid
# The password is valid if all criteria are met:
# a. Greater than 15 letters
# b. Have at least one capital letter
# c. Have at least one number
# d. Have at least one special char

import string

# user input
userPassword = input("Enter Password: ")

# initial declaration of variables
length = False
capLettersNum = 0
numbersNum = 0
specialChar = 0

# validation 
for char in userPassword:
        if len(userPassword) > 15:
            length = True
        if char.isupper():
            capLettersNum += 1
        if char.isnumeric():
            numbersNum += 1
        if char in set(string.punctuation):
            specialChar += 1

if length == True and capLettersNum > 0 and numbersNum > 0 and specialChar > 0:
    print("Password is Valid.")
else: 
    print("Password is Invalid.")
    