from importlib.metadata import files
import random       #for using random.choice function
import os
f = open("words.txt", "r")      #opening the file
content = f.read()              #reading the file
wordList = content.split("\n")  #storing the content of the file in the list
f.close()
f = open("wordList.txt","w")
for word in wordList:
    if(len(word) == 5):
        f.write(f"{word.upper()}\n")
f.close()       #closing the file
f = open("wordList.txt","r")
content = f.read()
filteredList = content.split('\n')
f.close()
def randomWord() :      #to generate random word
    return random.choice(filteredList)

def checkWord(word) :       #to check a valid dictionary word
    if(word in filteredList):
        return True
    else:
        return False

def removeWord(word):
    with open("wordList.txt", "r") as f:
        lines = f.readlines()
    with open("wordList.txt", "w") as f:
        for line in lines:
            if line.strip("\n") != word:
                f.write(line)
    if(fileSize()):
        try:
            resetWords()
        except:
            print("Reset words not working")

def resetWords():
    f = open("wordList","w")
    f.write(filteredList)
    f.close()

def fileSize():
    if os.stat("wordList.txt").st_size == 0 :
        return True
    else:
        return False