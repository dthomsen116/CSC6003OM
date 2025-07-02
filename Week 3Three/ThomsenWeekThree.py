# Imports (os for files, counter for counting functionality)
import os
from collections import Counter

# Global Variables (feel free to try out episodes 4-6)
filePath = "Week Three\EpisodeFour.txt"
text = ""

# Function to read the file and set the text to a global variable, used in the later functions
def readTextFile():
    global text
    with open(filePath, 'r') as file:
        text = file.read()

# Function to save the file, used in the later functions
def saveTextFile():
    with open(filePath, 'w') as file:
        file.write(text)

# Function to locate one word. This is used in single word count and replace word functions when locating the user input 
def getOneWord(prompt):
    while True:
        word = input(prompt).strip()
        if ' ' not in word and word != "":
            return word
        print("Please enter a single word.")

# Function to gather all the words in the text file then print the most common 5 words and the amount of times they come up.
def allWordCount():
    words = text.lower().split()
    count = Counter(words)
    mostCommon = count.most_common(5)
    for word, freq in mostCommon:
        print(f"{word.upper()} appears {freq} times")

# Function to take the user's input and see how many times the word comes up. This is done by making the whole text lowercase to standardize capitalization then searching for the input word. 
def singleWordCount():
    userWord = getOneWord(">>input Word: ").lower()
    words = text.lower().split()
    count = words.count(userWord)
    print(f"{userWord.upper()} appears {count} times!")

# Funtion to search the document for a word then replace it with another word. This is done the same way as the single word count function but with another loop for counting the amount of times the word comes up and replace it each time. 
def replaceWord():
    global text
    oneWord = getOneWord("Input the word to change: ").lower()
    replacement = getOneWord("Input what to change it to: ")

    words = text.split()
    newWords = []
    count = 0

    for word in words:
        if word.lower() == oneWord:
            newWords.append(replacement)
            count += 1
        else:
            newWords.append(word)

    text = ' '.join(newWords)
    saveTextFile()
    print(f"{count} copies of the word {oneWord.upper()} have been changed to {replacement.upper()}")


# Function to append user input text to the end of the document.
def addText():
    global text
    newText =  " " + input("Text to add: ")
    text += newText
    saveTextFile()
    print("Text added")

# Function to search for specific text to delete from the document. This is case specific unlike the previous as deleting data that is not specifically intended can be dangerous. 
def deleteText():
    global text
    toDel = input("Input the text to delete: ")
    if toDel in text:
        text = text.replace(toDel, "", 1)
        saveTextFile()
        print("Deletion Successful")
    else:
        print("Text not found")

# Function to search for a user input and add highlights to the word/phrase specified. 
def highlight():
    userWord = getOneWord("What word should be highlighted: ").lower()
    words = text.split()
    highlightedWords = []

    for word in words:
        if word.lower() == userWord:
            highlightedWords.append(f"\033[93m**{word}**\033[0m")
        else:
            highlightedWords.append(word)

    highlightText = ' '.join(highlightedWords)
    print("\nHighlighted Text:\n")
    print(highlightText)

# menu that loops and operates all of the functions. The first function reads the text file, then the other operations are available to use. 
def menu():
    readTextFile()
    while True:
        print("\n===Edit Menu===")
        print("1: Top 5 most common words")
        print("2: Single Word Frequency")
        print("3: Replace a word")
        print("4: Add Text")
        print("5: Delete Text")
        print("6: Highlight Text")
        print("0: Exit")
        print("===============")
        choice = int(input("Choose a function: "))

        if choice == 1:
            allWordCount()        
        elif choice == 2:
            singleWordCount()
        elif choice == 3:
            replaceWord()
        elif choice == 4:
            addText()
        elif choice == 5:
            deleteText()
        elif choice == 6:
            highlight()
        elif choice == 0:
            print("Exiting...")
            break
        else:
            print("Please enter a number to choose a function")

if __name__ == "__main__":
    menu()