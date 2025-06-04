import os
from collections import Counter

filePath = "Week Three\EpisodeFour.txt"
text = ""

def readTextFile():
    global text
    with open(filePath, 'r') as file:
        text = file.read()

def saveTextFile():
    with open(filePath, 'w') as file:
        file.write(text)

def getOneWord(prompt):
    while True:
        word = input(prompt).strip()
        if ' ' not in word and word != "":
            return word
        print("Please enter a single word.")

def allWordCount():
    words = text.lower().split()
    count = Counter(words)
    mostCommon = count.most_common(5)
    for word, freq in mostCommon:
        print(f"{word.upper()} appears {freq} times")

def singleWordCount():
    userWord = getOneWord(">>input Word: ").lower()
    words = text.lower().split()
    count = words.count(userWord)
    print(f"{userWord.upper()} appears {count} times!")

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


def addText():
    global text
    newText =  " " + input("Text to add: ")
    text += newText
    saveTextFile()
    print("Text added")

def deleteText():
    global text
    toDel = input("Input the text to delete: ")
    if toDel in text:
        text = text.replace(toDel, "", 1)
        saveTextFile()
        print("Deletion Successful")
    else:
        print("Text not found")

def highlight():
    userWord = getOneWord("What word should be highlighted: ")
    highlight = text.replace(userWord, f"**{userWord}**")
    print("\nHighlighted Text:\n")
    print(highlight)

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
            print("exiting...")
            break
        else:
            print("Please enter a number to choose a function")

if __name__ == "__main__":
    menu()