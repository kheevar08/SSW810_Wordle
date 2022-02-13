import random       #for using random.choice function
f = open("words.txt", "r")      #opening the file
content = f.read()              #reading the file
wordList = content.split("\n")  #storing the content of the file in the list
filteredList = []               #new list to store 5 letter dictionary words only
for word in wordList:
    if(len(word) == 5):
        filteredList.append(word.upper())
f.close()       #closing the file

def randomWord() :      #to generate random word
    return random.choice(filteredList)

def checkWord(word) :       #to check a valid dictionary word
    if(word in filteredList):
        return True
    else:
        return False