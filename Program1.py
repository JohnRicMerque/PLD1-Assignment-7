# Program 1:
# Create a program that ask for a sentence as input.
# Display the number of words, vowels and consonants in the input

def getWordsNum(char, text):
    count = 1
    for i in text:
        if char == i:
            count += 1
    return count

sentence = input("Enter a sentence: ")
wordsNum = getWordsNum(" ", sentence)
print(f"Number of Words: {wordsNum}")