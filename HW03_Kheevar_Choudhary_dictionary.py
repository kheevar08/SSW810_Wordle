from importlib.metadata import files
import random       #for using random.choice function
import os
class Dictionary:

    filteredList = []

    def __init__(self):   
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
        self.filteredList = content.split('\n')
        f.close()
    def randomWord(self) :      #to generate random word
        return random.choice(self.filteredList)

    def checkWord(self,word) :       #to check a valid dictionary word
        if(word in self.filteredList):
            return True
        else:
            return False

    def removeWord(self,word):
        with open("wordList.txt", "r") as f:
            lines = f.readlines()
        with open("wordList.txt", "w") as f:
            for line in lines:
                if line.strip("\n") != word:
                    f.write(line)
        if(self.fileSize()):
            try:
                self.resetWords()
            except:
                print("Reset words not working")

    def resetWords(self):
        f = open("wordList","w")
        f.write(self.filteredList)
        f.close()

    def fileSize(self):
        if os.stat("wordList.txt").st_size == 0 :
            return True
        else:
            return False