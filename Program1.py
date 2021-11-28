# Program 1:
# Create a program that ask for a sentence as input.
# Display the number of words, vowels and consonants in the input
import re

def getWordsNum(char, text):
    count = 1
    for i in text:
        if char == i:
            count += 1
    return count

# user input
sentence = input("Enter a sentence: ")

# Removing leading, trailing, and multiple whitespaces in the input
sentence = sentence.strip()
sentence = re.sub('  +', ' ', sentence)

# getting the number of words
wordsNum = getWordsNum(" ", sentence)
print(f"Number of words: {wordsNum}")
