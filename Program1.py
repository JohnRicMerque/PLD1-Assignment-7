# Program 1:
# Create a program that ask for a sentence as input.
# Display the number of words, vowels and consonants in the input

import re

# functions
def getWordsNum(spaces, text):
    count = 1
    for i in text:
        if spaces == i:
            count += 1
    return count

def getVowelsNum(vowels, text):
    text = text.lower()
    count = 0
    for i in text:
        if i in vowels:
            count += 1
    return count

def getConsonantsNum(consonants, text):
    text = text.lower()
    count = 0
    for i in text:
        if i in consonants:
            count += 1
    return count

# lists
vowelsList = ["a", "e", "i", "o", "u"]
consonantsList = [
    "b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w","x", "y", "z"
    ]
    
# user input
sentence = input("Enter a sentence: ")

# removing leading, trailing, and multiple whitespaces in the input
sentence = sentence.strip()
sentence = re.sub('  +', ' ', sentence)

# getting the number of words
wordsNum = getWordsNum(" ", sentence)
print(f"Number of words: {wordsNum}")

# getting the number of vowels
vowelsNum = getVowelsNum(vowelsList, sentence)
print(f"Number of vowels: {vowelsNum}")

# getting the number of consonants
consonantsNum = getConsonantsNum(consonantsList, sentence)
print(f"Number of consonants: {consonantsNum}")
